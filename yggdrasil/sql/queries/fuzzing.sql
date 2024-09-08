-- name: CreateFuzzing :one
INSERT INTO fuzzing (id, created_at, updated_at, part, condition, required)
VALUES ($1, $2, $3, $4, $5, $6)
RETURNING *;

-- name: GetFuzzingByID :one
SELECT *
FROM fuzzing
WHERE id = $1;

-- name: ListFuzzing :many
SELECT *
FROM fuzzing;

-- name: DeleteFuzzing :exec
DELETE
FROM fuzzing
WHERE id = $1;