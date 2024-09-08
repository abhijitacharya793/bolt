package handler

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/abhijitacharya793/bifrost/internal/database"
	"github.com/google/uuid"
)

func (apiCfg *apiConfig) handlerCreateQuery(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: Create Query")
	type parameters struct {
		Name  string    `json:"name"`
		Value string    `json:"value"`
		Api   uuid.UUID `json:"api"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	query, err := apiCfg.DB.CreateQuery(r.Context(), database.CreateQueryParams{
		ID:        uuid.New(),
		CreatedAt: time.Now().UTC(),
		UpdatedAt: time.Now().UTC(),
		Name:      params.Name,
		Value:     params.Value,
		Api:       params.Api,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create query: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseQueryToQuery(query))
}

func (apiCfg *apiConfig) handlerGetQueryByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: Get Query by ID")
	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	query, err := apiCfg.DB.GetQueryByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get query: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseQueryToQuery(query))
}

// LIST
func (apiCfg *apiConfig) handlerListQuery(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: List Query")
	query, err := apiCfg.DB.ListQuery(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get query: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseQueriesToQueries(query))
}
