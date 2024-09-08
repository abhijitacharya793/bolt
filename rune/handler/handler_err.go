package handler

import (
	"log"
	"net/http"
)

func handlerErr(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: /err")

	respondWithError(w, 400, "Something went wrong")
}
