cd bifrost
docker run --rm -v %cd%:/src -w /src kjconroy/sqlc generate

cd ../rune
docker run --rm -v %cd%:/src -w /src kjconroy/sqlc generate

cd ../valhalla
docker run --rm -v %cd%:/src -w /src kjconroy/sqlc generate

cd ../yggdrasil
docker run --rm -v %cd%:/src -w /src kjconroy/sqlc generate

cd ..