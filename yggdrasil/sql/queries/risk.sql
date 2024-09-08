-- name: CreateRisk :one
INSERT INTO risk (id, created_at, updated_at, name, abbreviation, description, remediation)
VALUES ($1, $2, $3, $4, $5, $6, $7)
RETURNING *;

-- name: GetRiskByID :one
SELECT *
FROM risk
WHERE id = $1;

-- name: ListRisk :many
SELECT *
FROM risk;

-- name: DeleteRisk :exec
DELETE
FROM risk
WHERE id = $1;