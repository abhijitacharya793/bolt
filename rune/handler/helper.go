package handler

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"encoding/xml"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"

	"github.com/google/uuid"
)

// Items Define struct to map XML data
type Items struct {
	XMLName xml.Name `xml:"items"`
	Items   []API    `xml:"item"`
}

type API struct {
	Url            string `xml:"url"`
	Host           string `xml:"host"`
	Port           string `xml:"port"`
	Protocol       string `xml:"protocol"`
	Method         string `xml:"method"`
	Path           string `xml:"path"`
	Extension      string `xml:"extension"`
	Request        string `xml:"request"`
	Status         string `xml:"status"`
	ResponseLength string `xml:"responselength"`
	MimeType       string `xml:"mimetype"`
	Response       string `xml:"response"`
	Comment        string `xml:"comment"`
}

type APIasJSON struct {
	Target          string `json:"target"`
	RootDomain      string `json:"rootDomain"`
	Domain          string `json:"domain"`
	Host            string `json:"host"`
	Port            string `json:"port"`
	Protocol        string `json:"protocol"`
	Method          string `json:"method"`
	Path            string `json:"path"`
	ProtocolVersion string `json:"protocolVersion"`
}

type Header struct {
	Name  string `json:"name"`
	Value string `json:"value"`
}

type Query struct {
	Name  string `json:"name"`
	Value string `json:"value"`
}

type Enrich struct {
	ApiId      uuid.UUID `json:"api_id"`
	Power      string    `json:"power"`
	Scope      string    `json:"scope"`
	Tasks      string    `json:"tasks"`
	Completion string    `json:"completion"`
	Status     string    `json:"status"`
}

// API CREATE
type ApiResponse struct {
	Status          string `json:"status"`
	Id              string `json:"id"`
	CreatedAt       string `json:"created_at"`
	UpdatedAt       string `json:"updated_at"`
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

// ################################################################################

func base64Decode(encodedRequest string) string {
	decodedBytes, err := base64.StdEncoding.DecodeString(encodedRequest)
	if err != nil {
		fmt.Println("Error decoding string:", err)
		return ""
	}

	// Convert the bytes to string
	decodedString := string(decodedBytes)
	return decodedString
}

func getPath(path string) string {
	parts := strings.Split(path, "?")
	result := parts[0]
	return result
}

func getRootDomain(host string) string {
	TLDs := []string{".com", ".org", ".net", ".gov", ".co.in", ".edu", ".info", ".biz", ".mobi", ".name", ".shop", ".io", ".app",
		".tv", ".co", ".me", "jobs", ".us", ".uk", ".ca", ".au", ".jp", ".de", ".fr", "in", ".cn", ".br", ".ru", ".mx",
		".ae", ".nz", ".za"}

	apiTLD := ""
	for _, tld := range TLDs {
		if strings.Contains(host, tld) {
			host = strings.Replace(host, tld, "", -1)
			apiTLD = tld
		}
	}

	if apiTLD == "" {
		panic("API Domain TLD Not Registered")
	}

	parts := strings.Split(host, ".")
	rootDomain := parts[len(parts)-1] + apiTLD
	return rootDomain
}

func getProtocolVersion(request string) string {
	lines := strings.Split(request, "\r\n")
	firstLine := lines[0]
	parts := strings.Split(firstLine, " ")
	protocolVersion := parts[len(parts)-1]
	return protocolVersion
}

func getBody(request string) string {
	bodyParts := strings.Split(request, "\r\n\r\n")

	if len(bodyParts) > 1 && bodyParts[1] != "" {
		body := bodyParts[1]
		return body
	}
	return "" // or return nil if you prefer
}

func getHeaders(request string) []Header {
	var headers []Header

	headerString := strings.Split(request, "\r\n")[1]

	if headerString != "" {
		header := strings.Split(headerString, "\r\n")
		for _, headerItem := range header {
			parts := strings.SplitN(headerItem, ":", 2)
			if len(parts) == 2 {
				headerMap := Header{
					Name:  strings.TrimSpace(parts[0]),
					Value: strings.TrimSpace(parts[1]),
				}
				headers = append(headers, headerMap)
			}
		}
	}
	return headers
}

func getParams(request string) []Query {
	var params []Query

	line1 := strings.Split(request, "\r\n")[0]
	line1Parts := strings.Split(line1, " ")
	if len(line1Parts) > 1 {
		urlParts := strings.Split(line1Parts[1], "?")
		if len(urlParts) > 1 {
			paramString := urlParts[1]
			paramPairs := strings.Split(paramString, "&")
			for _, paramPair := range paramPairs {
				parts := strings.SplitN(paramPair, "=", 2)
				if len(parts) == 2 {
					paramMap := Query{
						Name:  parts[0],
						Value: parts[1],
					}
					params = append(params, paramMap)
				}
			}
		}
	}

	return params
}

// ################################################################################

func parseXml(path string) Items {
	file, err := os.Open(path)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return Items{}
	}
	defer file.Close()

	// Parse XML data
	var items Items
	decoder := xml.NewDecoder(file)
	if err := decoder.Decode(&items); err != nil {
		fmt.Println("Error decoding XML:", err)
		return Items{}
	}

	// Print parsed data
	fmt.Printf("Number of APIs: %d\n", len(items.Items))

	return items
}

func parseApi(api API) (APIasJSON, []Header, []Query, string) {
	apiAsJson := APIasJSON{
		Target:          api.Url,
		RootDomain:      getRootDomain(api.Host),
		Domain:          api.Host,
		Host:            api.Host,
		Port:            api.Port,
		Protocol:        api.Protocol,
		Method:          api.Method,
		Path:            getPath(api.Path),
		ProtocolVersion: getProtocolVersion(base64Decode(api.Request)),
	}

	return apiAsJson, getHeaders(base64Decode(api.Request)), getParams(base64Decode(api.Request)), getBody(base64Decode(api.Request))
}

func saveApi(api APIasJSON, headers []Header, query []Query, body string, scope string) string {
	// API
	apiResponse := callAPIRequest(api, body)
	apiId := apiResponse.Id

	// HEADER
	for _, header := range headers {
		callHeaderRequest(header, apiId)
	}

	// QUERY
	for _, query := range query {
		callQueryRequest(query, apiId)
	}

	return apiId
}

func enrichScan(apiId string, scanId string, scanName string, power string, scope string) {
	// TODO: Call valhalla
	log.Println("Calling valhalla")
	apiUrl := "http://valhalla-api:8335/valhalla/v1/enricher"
	requestBody, err := json.Marshal(map[string]string{
		"api_id":    apiId,
		"scan_id":   scanId,
		"scan_name": scanName,
		"power":     power,
		"scope":     scope,
		"status":    "1",
	})
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return
	}
	request(apiUrl, requestBody)
}

func callAPIRequest(api APIasJSON, body string) ApiResponse {
	apiUrl := "http://bifrost-api:8333/bifrost/v1/api"
	requestBody, err := json.Marshal(map[string]string{
		"target":          api.Target,
		"rootDomain":      api.RootDomain,
		"domain":          api.Domain,
		"protocol":        api.Protocol,
		"protocolVersion": api.ProtocolVersion,
		"port":            api.Port,
		"method":          api.Method,
		"path":            api.Path,
		"body":            body,
	})
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return ApiResponse{}
	}
	var apiResponse ApiResponse
	requestResponse(apiUrl, requestBody, &apiResponse)
	return apiResponse
}

func callHeaderRequest(header Header, api string) {
	apiUrl := "http://bifrost-api:8333/bifrost/v1/headers"
	requestBody, err := json.Marshal(map[string]string{
		"name":  header.Name,
		"value": header.Value,
		"api":   api,
	})
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return
	}
	request(apiUrl, requestBody)
}

func callQueryRequest(query Query, api string) {
	apiUrl := "http://bifrost-api:8333/bifrost/v1/queries"
	requestBody, err := json.Marshal(map[string]string{
		"name":  query.Name,
		"value": query.Value,
		"api":   api,
	})
	if err != nil {
		fmt.Println("Error marshalling JSON:", err)
		return
	}
	request(apiUrl, requestBody)
}

func requestResponse(apiUrl string, requestBody []byte, apiResponse *ApiResponse) {
	resp := request(apiUrl, requestBody)
	defer resp.Body.Close()

	if err := json.NewDecoder(resp.Body).Decode(&apiResponse); err != nil {
		fmt.Println("Error decoding JSON:", err)
		return
	}
}

func request(apiUrl string, requestBody []byte) *http.Response {
	// Create a new HTTP POST request
	req, err := http.NewRequest("POST", apiUrl, bytes.NewBuffer(requestBody))
	if err != nil {
		fmt.Println("Error creating request:", err)
		return nil
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")

	// Create an HTTP client and send the request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		return nil
	}
	return resp
}
