cd bifrost/sql/schema
goose postgres postgres://postgres:postgres@localhost:5432/bolt up

cd ../../../rune/sql/schema
goose postgres postgres://postgres:postgres@localhost:5432/bolt up

cd ../../../valhalla/sql/schema
goose postgres postgres://postgres:postgres@localhost:5432/bolt up

cd ../../../yggdrasil/sql/schema
goose postgres postgres://postgres:postgres@localhost:5432/bolt up

cd ../../..