package handler

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/abhijitacharya793/yggdrasil/internal/database"
	"github.com/google/uuid"
)

// FUZZING
func (apiCfg *apiConfig) handlerCreateFuzzing(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: CreateFuzzing")

	type parameters struct {
		Part      string `json:"part"`
		Condition string `json:"condition"`
		Required  string `json:"required"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	api, err := apiCfg.DB.CreateFuzzing(r.Context(), database.CreateFuzzingParams{
		ID:        uuid.New(),
		CreatedAt: time.Now().UTC(),
		UpdatedAt: time.Now().UTC(),
		Part:      params.Part,
		Condition: params.Condition,
		Required:  params.Required,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseFuzzingToFuzzing(api))
}

func (apiCfg *apiConfig) handlerGetFuzzingByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetFuzzingByID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetFuzzingByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseFuzzingToFuzzing(api))
}

// LIST
func (apiCfg *apiConfig) handlerListFuzzing(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListFuzzing")
	api, err := apiCfg.DB.ListFuzzing(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseFuzzingsToFuzzings(api))
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteFuzzing(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteFuzzing")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteFuzzing(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuid.String())
}
