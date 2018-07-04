FROM ubuntu:18.04
RUN apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000