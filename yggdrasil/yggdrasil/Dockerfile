FROM python:3.10

WORKDIR /yggdrasil

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DISABLE_NUCLEI_TEMPLATES_PUBLIC_DOWNLOAD true

COPY ./requirements.txt /yggdrasil/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /yggdrasil/requirements.txt

COPY ./entrypoint.sh /yggdrasil/entrypoint.sh

COPY . /yggdrasil

ENTRYPOINT ["/yggdrasil/entrypoint.sh"]