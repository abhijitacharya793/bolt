package handler

import (
	"time"

	"github.com/abhijitacharya793/bifrost/internal/database"
	"github.com/google/uuid"
)

// API
type Api struct {
	ID              uuid.UUID `json:"id"`
	CreatedAt       time.Time `json:"created_at"`
	UpdatedAt       time.Time `json:"updated_at"`
	Target          string    `json:"target"`
	RootDomain      string    `json:"rootDomain"`
	Domain          string    `json:"domain"`
	Protocol        string    `json:"protocol"`
	ProtocolVersion string    `json:"protocolVersion"`
	Port            string    `json:"port"`
	Method          string    `json:"method"`
	Path            string    `json:"path"`
	Body            string    `json:"body"`
}

// ONE
func databaseApiToApi(dbApi database.Api) Api {
	return Api{
		ID:              dbApi.ID,
		CreatedAt:       dbApi.CreatedAt,
		UpdatedAt:       dbApi.UpdatedAt,
		Target:          dbApi.Target,
		RootDomain:      dbApi.RootDomain,
		Domain:          dbApi.Domain,
		Protocol:        dbApi.Protocol,
		ProtocolVersion: dbApi.ProtocolVersion,
		Port:            dbApi.Port,
		Method:          dbApi.Method,
		Path:            dbApi.Path,
		Body:            dbApi.Body,
	}
}

// MANY
func databaseApisToApis(dbApis []database.Api) []Api {
	var apis []Api

	for _, dbApi := range dbApis {
		api := databaseApiToApi(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// QUERY
type Query struct {
	ID        uuid.UUID `json:"id"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	Name      string    `json:"name"`
	Value     string    `json:"value"`
	Api       uuid.UUID `json:"api"`
}

// ONE
func databaseQueryToQuery(dbQuery database.Query) Query {
	return Query{
		ID:        dbQuery.ID,
		CreatedAt: dbQuery.CreatedAt,
		UpdatedAt: dbQuery.UpdatedAt,
		Name:      dbQuery.Name,
		Value:     dbQuery.Value,
		Api:       dbQuery.Api,
	}
}

// MANY
func databaseQueriesToQueries(dbQueries []database.Query) []Query {
	var queries []Query

	for _, dbQuery := range dbQueries {
		query := databaseQueryToQuery(dbQuery)
		queries = append(queries, query)
	}

	return queries
}

// HEADER
type Header struct {
	ID        uuid.UUID `json:"id"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	Name      string    `json:"name"`
	Value     string    `json:"value"`
	Api       uuid.UUID `json:"api"`
}

// ONE
func databaseHeaderToHeader(dbHeader database.Header) Header {
	return Header{
		ID:        dbHeader.ID,
		CreatedAt: dbHeader.CreatedAt,
		UpdatedAt: dbHeader.UpdatedAt,
		Name:      dbHeader.Name,
		Value:     dbHeader.Value,
		Api:       dbHeader.Api,
	}
}

// MANY
func databaseHeadersToHeaders(dbHeaders []database.Header) []Header {
	var headers []Header

	for _, dbHeader := range dbHeaders {
		header := databaseHeaderToHeader(dbHeader)
		headers = append(headers, header)
	}

	return headers
}
