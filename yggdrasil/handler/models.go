package handler

import (
	"time"

	"github.com/abhijitacharya793/yggdrasil/internal/database"
	"github.com/google/uuid"
)

// Tag
type Tag struct {
	ID        uuid.UUID `json:"id"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	Name      string    `json:"name"`
}

// ONE
func databaseTagToTag(dbApi database.Tag) Tag {
	return Tag{
		ID:        dbApi.ID,
		CreatedAt: dbApi.CreatedAt,
		UpdatedAt: dbApi.UpdatedAt,
		Name:      dbApi.Name,
	}
}

// MANY
func databaseTagsToTags(dbApis []database.Tag) []Tag {
	var apis []Tag

	for _, dbApi := range dbApis {
		api := databaseTagToTag(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// Fuzzing
type Fuzzing struct {
	ID        uuid.UUID `json:"id"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	Part      string    `json:"part"`
	Condition string    `json:"condition"`
	Required  string    `json:"required"`
}

// ONE
func databaseFuzzingToFuzzing(dbApi database.Fuzzing) Fuzzing {
	return Fuzzing{
		ID:        dbApi.ID,
		CreatedAt: dbApi.CreatedAt,
		UpdatedAt: dbApi.UpdatedAt,
		Part:      dbApi.Part,
		Condition: dbApi.Condition,
		Required:  dbApi.Required,
	}
}

// MANY
func databaseFuzzingsToFuzzings(dbApis []database.Fuzzing) []Fuzzing {
	var apis []Fuzzing

	for _, dbApi := range dbApis {
		api := databaseFuzzingToFuzzing(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// Risk
type Risk struct {
	ID           uuid.UUID `json:"id"`
	CreatedAt    time.Time `json:"created_at"`
	UpdatedAt    time.Time `json:"updated_at"`
	Name         string    `json:"name"`
	Abbreviation string    `json:"abbreviation"`
	Description  string    `json:"description"`
	Remediation  string    `json:"remediation"`
}

// ONE
func databaseRiskToRisk(dbApi database.Risk) Risk {
	return Risk{
		ID:           dbApi.ID,
		CreatedAt:    dbApi.CreatedAt,
		UpdatedAt:    dbApi.UpdatedAt,
		Name:         dbApi.Name,
		Abbreviation: dbApi.Abbreviation,
		Description:  dbApi.Description,
		Remediation:  dbApi.Remediation,
	}
}

// MANY
func databaseRisksToRisks(dbApis []database.Risk) []Risk {
	var apis []Risk

	for _, dbApi := range dbApis {
		api := databaseRiskToRisk(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// Vulnerability
type Vulnerability struct {
	ID               uuid.UUID `json:"id"`
	CreatedAt        time.Time `json:"created_at"`
	UpdatedAt        time.Time `json:"updated_at"`
	Name             string    `json:"name"`
	Risk             uuid.UUID `json:"risk"`
	Command          string    `json:"command"`
	Severity         string    `json:"severity"`
	StepsToReproduce string    `json:"steps_to_reproduce"`
	Power            string    `json:"power"`
}

// ONE
func databaseVulnerabilityToVulnerability(dbApi database.Vulnerability) Vulnerability {
	return Vulnerability{
		ID:               dbApi.ID,
		CreatedAt:        dbApi.CreatedAt,
		UpdatedAt:        dbApi.UpdatedAt,
		Name:             dbApi.Name,
		Risk:             dbApi.Risk,
		Command:          dbApi.Command,
		Severity:         dbApi.Severity,
		StepsToReproduce: dbApi.StepsToReproduce,
		Power:            dbApi.Power,
	}
}

// MANY
func databaseVulnerabilitysToVulnerabilitys(dbApis []database.Vulnerability) []Vulnerability {
	var apis []Vulnerability

	for _, dbApi := range dbApis {
		api := databaseVulnerabilityToVulnerability(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// VulnerabilityTag
type VulnerabilityTag struct {
	ID              uuid.UUID `json:"id"`
	VulnerabilityId uuid.UUID `json:"vulnerability_id"`
	TagId           uuid.UUID `json:"tag_id"`
}

// ONE
func databaseVulnerabilityTagToVulnerabilityTag(dbApi database.VulnerabilityTag) VulnerabilityTag {
	return VulnerabilityTag{
		ID:              dbApi.ID,
		VulnerabilityId: dbApi.VulnerabilityID,
		TagId:           dbApi.TagID,
	}
}

// MANY
func databaseVulnerabilityTagsToVulnerabilityTags(dbApis []database.VulnerabilityTag) []VulnerabilityTag {
	var apis []VulnerabilityTag

	for _, dbApi := range dbApis {
		api := databaseVulnerabilityTagToVulnerabilityTag(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// VulnerabilityFuzzing
type VulnerabilityFuzzing struct {
	ID              uuid.UUID `json:"id"`
	VulnerabilityId uuid.UUID `json:"vulnerability_id"`
	FuzzingId       uuid.UUID `json:"fuzzing_id"`
}

// ONE
func databaseVulnerabilityFuzzingToVulnerabilityFuzzing(dbApi database.VulnerabilityFuzzing) VulnerabilityFuzzing {
	return VulnerabilityFuzzing{
		ID:              dbApi.ID,
		VulnerabilityId: dbApi.VulnerabilityID,
		FuzzingId:       dbApi.FuzzingID,
	}
}

// MANY
func databaseVulnerabilityFuzzingsToVulnerabilityFuzzings(dbApis []database.VulnerabilityFuzzing) []VulnerabilityFuzzing {
	var apis []VulnerabilityFuzzing

	for _, dbApi := range dbApis {
		api := databaseVulnerabilityFuzzingToVulnerabilityFuzzing(dbApi)
		apis = append(apis, api)
	}

	return apis
}

// Template
type Template struct {
	ID            uuid.UUID `json:"id"`
	CreatedAt     time.Time `json:"created_at"`
	UpdatedAt     time.Time `json:"updated_at"`
	Vulnerability uuid.UUID `json:"vulnerability"`
	Path          string    `json:"path"`
}

// ONE
func databaseTemplateToTemplate(dbApi database.Template) Template {
	return Template{
		ID:            dbApi.ID,
		CreatedAt:     dbApi.CreatedAt,
		UpdatedAt:     dbApi.UpdatedAt,
		Vulnerability: dbApi.Vulnerability,
		Path:          dbApi.Path,
	}
}

// MANY
func databaseTemplatesToTemplates(dbApis []database.Template) []Template {
	var apis []Template

	for _, dbApi := range dbApis {
		api := databaseTemplateToTemplate(dbApi)
		apis = append(apis, api)
	}

	return apis
}
