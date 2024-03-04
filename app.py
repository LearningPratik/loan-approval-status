import uvicorn
import numpy as np
from fastapi import FastAPI
import schemas
import pickle

app = FastAPI()
pickle_in = open("models/svm-clf.pkl","rb")
classifier=pickle.load(pickle_in)

@app.post('/predict')
def predict_loan(data: schemas.Status):
    data = data.model_dump()
    married = data['married']
    if married == 'yes':
       married = 1
    else:
       married = 0

    gender = data['gender']
    if gender == 'male':
       gender = 0
    else:
       gender = 1

    self_employed = data['self_employed']
    if self_employed == 'yes':
       self_employed = 1
    else:
       self_employed = 0

    education = data['education']
    if education == 'graduate':
       education = 1
    else:
       education = 0
    amount = data['amount']
    credit_history = data['credit_history']
    
    
    pred = np.array([[married, gender, self_employed, education, amount, credit_history]]).reshape(1, -1)
    predictions = classifier.predict(pred)
    if predictions == 'Y':
      predictions = 'loan approved'
    else:
      predictions = 'loan not approved'
    return {
      'predictions' : predictions
    }

@app.get('/{name}')
def get_name(name: str):
  return {'text' : f"Hello, {name}"}


if __name__ == '__main__':
   uvicorn.run(app,host="127.0.0.1",port=8000)