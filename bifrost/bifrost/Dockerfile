FROM python:3.10

WORKDIR /bifrost

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /bifrost/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /bifrost/requirements.txt

COPY ./entrypoint.sh /bifrost/entrypoint.sh

COPY . /bifrost

# ENTRYPOINT ["/bifrost/entrypoint.sh"]
CMD ["bash"]
