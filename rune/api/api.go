package main

import (
	"github.com/abhijitacharya793/rune/handler"
	"github.com/gookit/config/v2"
	"github.com/gookit/config/v2/yaml"
)

func main() {
	config.WithOptions(config.ParseEnv)
	config.AddDriver(yaml.Driver)

	err := config.LoadFiles("config/dev.yml")
	if err != nil {
		panic(err)
	}

	handler.Handle(config.String("port"), config.String("db_url"))
}
