package handler

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/abhijitacharya793/valhalla/internal/database"
	"github.com/google/uuid"
)

// "1" - "Queued"
// "2" - "Running"
// "3" - "Successful"
// "4" - "Failed"

func (apiCfg *apiConfig) handlerCreateEnricher(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: CreateEnricher")

	type parameters struct {
		ApiId      uuid.UUID `json:"api_id"`
		ScanId     uuid.UUID `json:"scan_id"`
		ScanName   string    `json:"scan_name"`
		Power      string    `json:"power"`
		Scope      string    `json:"scope"`
		Tasks      string    `json:"tasks"`
		Completion string    `json:"completion"`
		Status     string    `json:"status"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	api, err := apiCfg.DB.CreateEnricher(r.Context(), database.CreateEnricherParams{
		ID:         uuid.New(),
		CreatedAt:  time.Now().UTC(),
		UpdatedAt:  time.Now().UTC(),
		ApiID:      params.ApiId,
		ScanID:     params.ScanId,
		ScanName:   params.ScanName,
		Power:      params.Power,
		Scope:      params.Scope,
		Tasks:      params.Tasks,
		Completion: params.Completion,
		Status:     params.Status,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseEnricherToEnricher(api))
}

func (apiCfg *apiConfig) handlerGetEnricherByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetEnricherByID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetEnricherByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseEnricherToEnricher(api))
}

func (apiCfg *apiConfig) handlerGetEnricherByScanID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetEnricherByScanID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetEnricherByScanID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseEnrichersToEnrichers(api))
}

func (apiCfg *apiConfig) handlerGetEnricherByStatus(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetEnricherByStatus")

	api, err := apiCfg.DB.GetEnricherByStatus(r.Context(), r.URL.Query().Get("status"))
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseEnrichersToEnrichers(api))
}

// LIST
func (apiCfg *apiConfig) handlerListEnricher(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListEnricher")
	api, err := apiCfg.DB.ListEnricher(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseEnrichersToEnrichers(api))
}

// UPDATE
func (apiCfg *apiConfig) handlerUpdateEnricher(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: UpdateEnricher")

	// Parse the Enricher ID from the request URL
	enricherID, err := uuid.Parse(r.URL.Query().Get("id"))
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Invalid Enricher ID: %v", err))
		return
	}

	// Define the same parameters structure used in the creation handler
	type parameters struct {
		ScanName   string `json:"scan_name"`
		Power      string `json:"power"`
		Scope      string `json:"scope"`
		Tasks      string `json:"tasks"`
		Completion string `json:"completion"`
		Status     string `json:"status"`
	}

	// Decode the JSON body into the parameters struct
	decoder := json.NewDecoder(r.Body)
	params := parameters{}
	err = decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error parsing JSON: %v", err))
		return
	}

	// Perform the update operation
	err = apiCfg.DB.UpdateEnricher(r.Context(), database.UpdateEnricherParams{
		ID:         enricherID,
		UpdatedAt:  time.Now().UTC(),
		ScanName:   params.ScanName,
		Power:      params.Power,
		Scope:      params.Scope,
		Tasks:      params.Tasks,
		Completion: params.Completion,
		Status:     params.Status,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't update Enricher: %v", err))
		return
	}

	// Return success response
	respondWithString(w, 200, "Updated successfully")
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteEnricher(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteEnricher")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteEnricher(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuid.String())
}
