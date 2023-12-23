FROM python:3.10

WORKDIR /asgard

RUN apt-get update -y
RUN apt-get install docker.io -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /asgard/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /asgard/requirements.txt

COPY ./entrypoint.sh /asgard/entrypoint.sh

COPY . /asgard

ENTRYPOINT ["/asgard/entrypoint.sh"]