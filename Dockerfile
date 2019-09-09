# base image
FROM python:3.7.3-alpine

# set working directory
WORKDIR /src/app

# add and install requirements
COPY ./requirements.txt /src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /src/app

# run service
CMD python3 /src/app/spotty.py