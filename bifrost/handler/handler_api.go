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

func (apiCfg *apiConfig) handlerCreateAPI(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: CreateAPI")

	type parameters struct {
		Target          string `json:"target"`
		RootDomain      string `json:"rootDomain"`
		Domain          string `json:"domain"`
		Protocol        string `json:"protocol"`
		ProtocolVersion string `json:"protocolVersion"`
		Port            string `json:"port"`
		Method          string `json:"method"`
		Path            string `json:"path"`
		Body            string `json:"body"`
	}

	decoder := json.NewDecoder(r.Body)

	params := parameters{}
	err := decoder.Decode(&params)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Error passing JSON: %v", err))
		return
	}

	api, err := apiCfg.DB.CreateApi(r.Context(), database.CreateApiParams{
		ID:              uuid.New(),
		CreatedAt:       time.Now().UTC(),
		UpdatedAt:       time.Now().UTC(),
		Target:          params.Target,
		RootDomain:      params.RootDomain,
		Domain:          params.Domain,
		Protocol:        params.Protocol,
		ProtocolVersion: params.ProtocolVersion,
		Port:            params.Port,
		Method:          params.Method,
		Path:            params.Path,
		Body:            params.Body,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}

	respondWithJSON(w, 200, databaseApiToApi(api))
}

func (apiCfg *apiConfig) handlerGetAPIByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetAPIByID")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetApiByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseApiToApi(api))
}

// LIST
func (apiCfg *apiConfig) handlerListAPI(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListAPI")
	api, err := apiCfg.DB.ListApi(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseApisToApis(api))
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteAPI(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteAPI")

	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteApi(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuid.String())
}

// REQUEST
func (apiCfg *apiConfig) handlerAPIRequest(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: APIRequest")
	uuid, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetApiByID(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}

	queries, err := apiCfg.DB.GetQueryByApi(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get query: %v", err))
		return
	}

	var query_string = ""
	for _, query := range queries {
		query_string += query.Name
		query_string += "="
		query_string += query.Value
		query_string += "&"
	}

	headers, err := apiCfg.DB.GetHeaderByApi(r.Context(), uuid)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get header: %v", err))
		return
	}

	var header_string = ""
	for _, header := range headers {
		header_string += header.Name
		header_string += ": "
		header_string += header.Value
		header_string += "\r\n"
	}

	formattedStringResponse := fmt.Sprintf("%v %v?%v %v\r\n%v\r\n", api.Method, api.Path, query_string, api.ProtocolVersion, header_string)

	respondWithString(w, 200, formattedStringResponse)
}
