package handler

import (
	"time"

	"github.com/abhijitacharya793/rune/internal/database"
	"github.com/google/uuid"
)

// BURP EXPORT
type BurpExport struct {
	ID         uuid.UUID `json:"id"`
	CreatedAt  time.Time `json:"created_at"`
	UpdatedAt  time.Time `json:"updated_at"`
	Name       string    `json:"name"`
	Scope      string    `json:"scope"`
	Power      string    `json:"power"`
	BurpExport string    `json:"burpExport"`
}

// ONE
func databaseBurpExportToBurpExport(dbApi database.BurpExport) BurpExport {
	return BurpExport{
		ID:         dbApi.ID,
		CreatedAt:  dbApi.CreatedAt,
		UpdatedAt:  dbApi.UpdatedAt,
		Name:       dbApi.Name,
		Scope:      dbApi.Scope,
		Power:      dbApi.Power,
		BurpExport: dbApi.Burpexport,
	}
}

// MANY
func databaseBurpExportsToBurpExports(dbApis []database.BurpExport) []BurpExport {
	var burpExports []BurpExport

	for _, dbApi := range dbApis {
		burpExport := databaseBurpExportToBurpExport(dbApi)
		burpExports = append(burpExports, burpExport)
	}

	return burpExports
}
