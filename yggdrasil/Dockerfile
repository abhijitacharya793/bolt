FROM golang:alpine as build

WORKDIR /yggdrasil
COPY . /yggdrasil
RUN go build -o /bin/main api/api.go

FROM scratch
COPY --from=build /bin/main /bin/main
COPY --from=build /yggdrasil/config/ /yggdrasil/config/
WORKDIR /yggdrasil
CMD [ "/bin/main" ]