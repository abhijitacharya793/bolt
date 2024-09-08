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

// TAG
func (apiCfg *apiConfig) handlerCreateTag(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: CreateTag")

	type parameters struct {
		ID        uuid.UUID `json:"id"`
		CreatedAt time.Time `json:"created_at"`
		UpdatedAt time.Time `json:"updated_at"`
		Name      string    `json:"name"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	api, err := apiCfg.DB.CreateTag(r.Context(), database.CreateTagParams{
		ID:        uuid.New(),
		CreatedAt: time.Now().UTC(),
		UpdatedAt: time.Now().UTC(),
		Name:      params.Name,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseTagToTag(api))
}

func (apiCfg *apiConfig) handlerGetTagByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetTagByID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetTagByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseTagToTag(api))
}

// LIST
func (apiCfg *apiConfig) handlerListTag(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListTag")
	api, err := apiCfg.DB.ListTag(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseTagsToTags(api))
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteTag(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteTag")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteTag(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuid.String())
}
