FROM python:3.10

WORKDIR /hiemdall

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DISABLE_NUCLEI_TEMPLATES_PUBLIC_DOWNLOAD true

COPY ./requirements.txt /hiemdall/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /hiemdall/requirements.txt

COPY ./entrypoint.sh /hiemdall/entrypoint.sh

COPY . /hiemdall

ENTRYPOINT ["/hiemdall/entrypoint.sh"]