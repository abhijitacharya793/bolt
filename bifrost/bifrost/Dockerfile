FROM python:3.10

WORKDIR /bifrost

COPY ./requirments.txt /bifrost/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /bifrost/requirements.txt

COPY . /bifrost

CMD ["python","manage.py","runserver","0.0.0.0:8333"]
