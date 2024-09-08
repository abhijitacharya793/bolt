package handler

import (
	"log"
	"net/http"
)

func handlerReadiness(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: /healthz")
	var hz Healthz
	hz.Server = "OK"
	hz.Database = "OK"

	respondWithJSON(w, 200, hz)
}
