#!/bin/bash

goose postgres postgres://postgres:postgres@db:5432/bolt up

exec "$@"