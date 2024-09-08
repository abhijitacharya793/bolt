package handler

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/abhijitacharya793/rune/internal/database"
	"github.com/google/uuid"
)

func (apiCfg *apiConfig) handlerUploadBurpExport(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: Upload")

	// Parse multipart form data to get the file and other parameters
	err := r.ParseMultipartForm(10 << 20) // 10 MB max
	if err != nil {
		respondWithError(w, http.StatusBadRequest, fmt.Sprintf("Error parsing form: %v", err))
		return
	}

	// Retrieve the file from the form data
	file, handler, err := r.FormFile("burpExport")
	if err != nil {
		respondWithError(w, http.StatusBadRequest, fmt.Sprintf("Error retrieving file: %v", err))
		return
	}

	defer file.Close()

	// Generate a random filename to store the uploaded file
	randomFilename := uuid.New().String() + filepath.Ext(handler.Filename)
	filePath := filepath.Join("/rune/uploads/", randomFilename) // Replace with your actual upload directory path

	// Create the file on disk
	f, err := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, fmt.Sprintf("Error creating file: %v", err))
		return
	}
	defer f.Close()

	// Copy the file content from request to the newly created file
	_, err = io.Copy(f, file)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, fmt.Sprintf("Error copying file: %v", err))
		return
	}

	name := r.FormValue("name")
	scope := r.FormValue("scope")
	power := r.FormValue("power")

	burpExport, err := apiCfg.DB.CreateBurpExport(r.Context(), database.CreateBurpExportParams{
		ID:         uuid.New(),
		CreatedAt:  time.Now().UTC(),
		UpdatedAt:  time.Now().UTC(),
		Name:       name,
		Scope:      scope,
		Power:      power,
		Burpexport: filePath,
	})
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't create API: %v", err))
		return
	}
	go parseBurpExport(burpExport.ID.String(), scope, name, power, filePath)

	respondWithJSON(w, 200, databaseBurpExportToBurpExport(burpExport))
}

func parseBurpExport(scanId string, scopeString string, scanName string, power string, filePath string) {
	apiStrings := parseXml(filePath)
	for _, apiString := range apiStrings.Items {
		api, headers, query, body := parseApi(apiString)

		scopes := strings.Split(scopeString, "\n")

		found := false
		for _, scope := range scopes {
			// Step 3: Check if rootDomain matches the current scope
			if api.RootDomain == scope {
				apiId := saveApi(api, headers, query, body, scope)
				// ENRICH SAVED API IN VALHALLA
				fmt.Println("###################################")
				fmt.Println(scanName)
				fmt.Println("###################################")
				if apiId != "-1" {
					enrichScan(apiId, scanId, scanName, power, scope)
				}
				found = true
				break
			} else {
				log.Printf("No match found: %s does not match %s\n", api.RootDomain, scope)
			}
		}
		if !found {
			fmt.Printf("No match found for %s\n", api.RootDomain)
		}
	}
}

func (apiCfg *apiConfig) handlerGetAPIByID(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: GetAPIByID")

	uuidValue, _ := uuid.Parse(r.URL.Query().Get("id"))

	api, err := apiCfg.DB.GetBurpExportByID(r.Context(), uuidValue)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get api: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseBurpExportToBurpExport(api))
}

// LIST
func (apiCfg *apiConfig) handlerListAPI(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: ListAPI")
	api, err := apiCfg.DB.ListBurpExport(r.Context())
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithJSON(w, 200, databaseBurpExportsToBurpExports(api))
}

// DELETE
func (apiCfg *apiConfig) handlerDeleteAPI(w http.ResponseWriter, r *http.Request) {
	log.Println("Endpoint Hit: DeleteAPI")

	uuidValue, _ := uuid.Parse(r.URL.Query().Get("id"))

	err := apiCfg.DB.DeleteBurpExport(r.Context(), uuidValue)
	if err != nil {
		respondWithError(w, 400, fmt.Sprintf("Couldn't get apis: %v", err))
		return
	}
	respondWithString(w, 200, "Deleted successfully: "+uuidValue.String())
}
