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

// RISK
func (apiCfg *apiConfig) handlerCreateRisk(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: CreateRisk")

	type parameters struct {
		Name         string `json:"name"`
		Abbreviation string `json:"abbreviation"`
		Description  string `json:"description"`
		Remediation  string `json:"remediation"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	api, err := apiCfg.DB.CreateRisk(r.Context(), database.CreateRiskParams{
		ID:           uuid.New(),
		CreatedAt:    time.Now().UTC(),
		UpdatedAt:    time.Now().UTC(),
		Name:         params.Name,
		Abbreviation: params.Abbreviation,
		Description:  params.Description,
		Remediation:  params.Remediation,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseRiskToRisk(api))
}

func (apiCfg *apiConfig) handlerGetRiskByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetRiskByID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetRiskByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseRiskToRisk(api))
}

// LIST
func (apiCfg *apiConfig) handlerListRisk(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListRisk")
	api, err := apiCfg.DB.ListRisk(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseRisksToRisks(api))
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteRisk(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteRisk")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteRisk(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuid.String())
}
