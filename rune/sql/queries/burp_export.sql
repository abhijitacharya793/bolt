-- name: CreateBurpExport :one
INSERT INTO burp_export (id, created_at, updated_at, name, scope, power, burpExport)
VALUES ($1, $2, $3, $4, $5, $6, $7)
RETURNING *;

-- name: GetBurpExportByID :one
SELECT *
FROM burp_export
WHERE id = $1;

-- name: ListBurpExport :many
SELECT *
FROM burp_export;

-- name: DeleteBurpExport :exec
DELETE
FROM burp_export
WHERE id = $1;