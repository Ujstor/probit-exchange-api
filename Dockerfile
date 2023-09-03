FROM python:3.8-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "gunicorn", "main:app", "--bind=0.0.0.0:5000"]