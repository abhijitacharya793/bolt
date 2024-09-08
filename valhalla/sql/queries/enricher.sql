-- name: CreateEnricher :one
INSERT INTO enricher (id, created_at, updated_at, api_id, scan_id, scan_name, power, scope, tasks, completion, status)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
RETURNING *;

-- name: GetEnricherByID :one
SELECT *
FROM enricher
WHERE id = $1;

-- name: GetEnricherByScanID :many
SELECT *
FROM enricher
WHERE scan_id = $1;

-- name: GetEnricherByStatus :many
SELECT *
FROM enricher
WHERE status = $1;

-- name: ListEnricher :many
SELECT *
FROM enricher;

-- name: UpdateEnricher :one

-- name: DeleteEnricher :exec
DELETE
FROM enricher
WHERE id = $1;