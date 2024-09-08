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

// TEMPLATE
func (apiCfg *apiConfig) handlerCreateTemplate(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: CreateTemplate")

	type parameters struct {
		Vulnerability uuid.UUID `json:"vulnerability"`
		Path          string    `json:"path"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	api, err := apiCfg.DB.CreateTemplate(r.Context(), database.CreateTemplateParams{
		ID:            uuid.New(),
		CreatedAt:     time.Now().UTC(),
		UpdatedAt:     time.Now().UTC(),
		Vulnerability: params.Vulnerability,
		Path:          params.Path,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseTemplateToTemplate(api))
}

func (apiCfg *apiConfig) handlerGetTemplateByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetTemplateByID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetTemplateByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseTemplateToTemplate(api))
}

// LIST
func (apiCfg *apiConfig) handlerListTemplate(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListTemplate")
	api, err := apiCfg.DB.ListTemplate(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseTemplatesToTemplates(api))
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteTemplate(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteTemplate")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteTemplate(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuid.String())
}
