FROM google/cloud-sdk:latest
RUN mkdir /code
WORKDIR /code

RUN apt-get update -y && apt-get install build-essential checkinstall python3-pip redis-server -y
ADD requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
ADD . /code/
