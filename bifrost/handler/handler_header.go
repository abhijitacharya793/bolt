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

func (apiCfg *apiConfig) handlerCreateHeader(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: Create Header")
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

	header, err := apiCfg.DB.CreateHeader(r.Context(), database.CreateHeaderParams{
		ID:        uuid.New(),
		CreatedAt: time.Now().UTC(),
		UpdatedAt: time.Now().UTC(),
		Name:      params.Name,
		Value:     params.Value,
		Api:       params.Api,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create Header: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseHeaderToHeader(header))
}

func (apiCfg *apiConfig) handlerGetHeaderByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: Get Header")
	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	header, err := apiCfg.DB.GetHeaderByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get Header: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseHeaderToHeader(header))
}

// LIST
func (apiCfg *apiConfig) handlerListHeader(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: List Header")
	header, err := apiCfg.DB.ListHeader(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseHeadersToHeaders(header))
}
