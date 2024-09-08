package handler

import (
	"time"

	"github.com/abhijitacharya793/valhalla/internal/database"
	"github.com/google/uuid"
)

// Enricher
type Enricher struct {
	ID         uuid.UUID `json:"id"`
	CreatedAt  time.Time `json:"created_at"`
	UpdatedAt  time.Time `json:"updated_at"`
	ApiId      uuid.UUID `json:"api_id"`
	ScanId     uuid.UUID `json:"scan_id"`
	ScanName   string    `json:"scan_name"`
	Power      string    `json:"power"`
	Scope      string    `json:"scope"`
	Tasks      string    `json:"tasks"`
	Completion string    `json:"completion"`
	Status     string    `json:"status"`
}

// ONE
func databaseEnricherToEnricher(dbApi database.Enricher) Enricher {
	return Enricher{
		ID:         dbApi.ID,
		CreatedAt:  dbApi.CreatedAt,
		UpdatedAt:  dbApi.UpdatedAt,
		ApiId:      dbApi.ApiID,
		ScanId:     dbApi.ScanID,
		ScanName:   dbApi.ScanName,
		Power:      dbApi.Power,
		Scope:      dbApi.Scope,
		Tasks:      dbApi.Tasks,
		Completion: dbApi.Completion,
		Status:     dbApi.Status,
	}
}

// MANY
func databaseEnrichersToEnrichers(dbApis []database.Enricher) []Enricher {
	var apis []Enricher

	for _, dbApi := range dbApis {
		api := databaseEnricherToEnricher(dbApi)
		apis = append(apis, api)
	}

	return apis
}
