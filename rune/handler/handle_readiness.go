package handler

import (
	"log"
	"net/http"
)

type Healthz struct {
	Server   string `json:"server"`
	Database string `json:"database"`
}

func handlerReadiness(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: /healthz")
	var hz Healthz
	hz.Server = "OK"
	hz.Database = "OK"

	respondWithJSON(w, 200, hz)
}
