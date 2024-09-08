package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

// type APIasJSON struct {
// 	Target          string `json:"target"`
// 	RootDomain      string `json:"rootDomain"`
// 	Domain          string `json:"domain"`
// 	Host            string `json:"host"`
// 	Port            string `json:"port"`
// 	Protocol        string `json:"protocol"`
// 	Method          string `json:"method"`
// 	Path            string `json:"path"`
// 	ProtocolVersion string `json:"protocolVersion"`
// }

// API CREATE
// type ApiResponse struct {
// 	Status          string `json:"status"`
// 	Id              string `json:"id"`
// 	CreatedAt       string `json:"created_at"`
// 	UpdatedAt       string `json:"updated_at"`
// 	Target          string `json:"target"`
// 	RootDomain      string `json:"rootDomain"`
// 	Domain          string `json:"domain"`
// 	Protocol        string `json:"protocol"`
// 	ProtocolVersion string `json:"protocolVersion"`
// 	Port            string `json:"port"`
// 	Method          string `json:"method"`
// 	Path            string `json:"path"`
// 	Body            string `json:"body"`
// }

type EnricherResponse struct {
	Id         string `json:"id"`
	CreatedAt  string `json:"created_at"`
	UpdatedAt  string `json:"updated_at"`
	ApiID      string `json:"api_id"`
	ScanID     string `json:"scan_id"`
	ScanName   string `json:"scan_name"`
	Power      string `json:"power"`
	Scope      string `json:"scope"`
	Tasks      string `json:"tasks"`
	Completion string `json:"completion"`
	Status     string `json:"status"`
}

// func request(apiUrl string, requestBody []byte) *http.Response {
// 	// Create a new HTTP POST request
// 	req, err := http.NewRequest("POST", apiUrl, bytes.NewBuffer(requestBody))
// 	if err != nil {
// 		fmt.Println("Error creating request:", err)
// 		return nil
// 	}

// 	// Set headers
// 	req.Header.Set("Content-Type", "application/json")

// 	// Create an HTTP client and send the request
// 	client := &http.Client{}
// 	resp, err := client.Do(req)
// 	if err != nil {
// 		fmt.Println("Error sending request:", err)
// 		return nil
// 	}
// 	return resp
// }

func requestGet(apiUrl string) (*http.Response, error) {
	req, err := http.NewRequest("GET", apiUrl, nil)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")
	return (&http.Client{}).Do(req)
}

// func requestResponse(apiUrl string, requestBody []byte, apiResponse *ApiResponse) {
// 	resp := request(apiUrl, requestBody)
// 	defer resp.Body.Close()

// 	if err := json.NewDecoder(resp.Body).Decode(&apiResponse); err != nil {
// 		fmt.Println("Error decoding JSON:", err)
// 		return
// 	}
// }

func enricherRequestResponse(apiUrl string) ([]EnricherResponse, error) {
	resp, err := requestGet(apiUrl)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var enricherResponse []EnricherResponse
	if err := json.NewDecoder(resp.Body).Decode(&enricherResponse); err != nil {
		return nil, err
	}
	return enricherResponse, nil
}

// func callAPIRequest(api APIasJSON, body string) ApiResponse {
// 	apiUrl := "http://bifrost-api:8333/bifrost/v1/api"
// 	requestBody, err := json.Marshal(map[string]string{
// 		"target":          api.Target,
// 		"rootDomain":      api.RootDomain,
// 		"domain":          api.Domain,
// 		"protocol":        api.Protocol,
// 		"protocolVersion": api.ProtocolVersion,
// 		"port":            api.Port,
// 		"method":          api.Method,
// 		"path":            api.Path,
// 		"body":            body,
// 	})
// 	if err != nil {
// 		fmt.Println("Error marshalling JSON:", err)
// 		return ApiResponse{}
// 	}
// 	var apiResponse ApiResponse
// 	requestResponse(apiUrl, requestBody, &apiResponse)
// 	return apiResponse
// }

func callValhallaEnricher(status string) (string, string, string, error) {
	apiUrl := "http://host.docker.internal:8335/valhalla/v1/enricher/status?status=" + status
	enricherResponse, err := enricherRequestResponse(apiUrl)
	if err != nil || len(enricherResponse) == 0 {
		return "", "", "", err
	}
	return enricherResponse[0].ApiID, enricherResponse[0].ScanID, enricherResponse[0].Tasks, nil
}

// "1" - "Queued"
// "2" - "Running"
// "3" - "Successful"
// "4" - "Failed"

func main() {
	ticker := time.NewTicker(30 * time.Second)
	defer ticker.Stop()

	for range ticker.C {
		// Get all running tasks
		apiId, _, _, err := callValhallaEnricher("2")
		if err != nil {
			fmt.Println("Error:", err)
		} else {
			if len(apiId) > 0 {
				// If task is already running, dont continue
				fmt.Println("A Job is already running: ", apiId)
			} else {
				apiId, scanId, tasks, err := callValhallaEnricher("1")
				if err != nil {
					fmt.Println("Error:", err)
				} else {
					fmt.Println("Starting queued task: ", apiId, tasks, scanId)
					// TODO: GET API OF ANY QUEUED TASK AND TRIGGER SCANS

				}
			}
		}
	}
}
