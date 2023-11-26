FROM python:3.10

WORKDIR /rune

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /rune/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /rune/requirements.txt

COPY ./entrypoint.sh /rune/entrypoint.sh

COPY . /rune

ENTRYPOINT ["/rune/entrypoint.sh"]