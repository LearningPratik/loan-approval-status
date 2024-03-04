# base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR '/app'

COPY requirements.txt .
# Download and install dependencies
# Install some dependencies
RUN pip install -r requirements.txt

COPY . .

CMD uvicorn app:app --reload
