FROM alpine:latest

WORKDIR /db

RUN apk add --no-cache bash

COPY ./bifrost/sql/schema/001_api.sql /db/001_api.sql
COPY ./bifrost/sql/schema/002_query.sql /db/002_query.sql
COPY ./bifrost/sql/schema/003_header.sql /db/003_header.sql
COPY ./rune/sql/schema/004_burp_export.sql /db/004_burp_export.sql
COPY ./valhalla/sql/schema/005_enricher.sql /db/005_enricher.sql
COPY ./yggdrasil/sql/schema/006_risk.sql /db/006_risk.sql

COPY ./postgresql/entrypoint.sh /db/entrypoint.sh

RUN apk add --no-cache curl
RUN curl -L https://github.com/pressly/goose/releases/download/v3.21.1/goose_linux_x86_64 -o /usr/local/bin/goose && chmod +x /usr/local/bin/goose

ENTRYPOINT ["/db/entrypoint.sh"]