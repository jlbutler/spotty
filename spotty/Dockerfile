FROM python:3.7.3-alpine
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "app:app", "--config=config.py"]