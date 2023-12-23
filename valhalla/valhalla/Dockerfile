FROM python:3.10

WORKDIR /valhalla

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /valhalla/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /valhalla/requirements.txt

COPY ./entrypoint.sh /valhalla/entrypoint.sh

COPY . /valhalla

ENTRYPOINT ["/valhalla/entrypoint.sh"]