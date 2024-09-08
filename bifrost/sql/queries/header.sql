-- name: CreateHeader :one
INSERT INTO header (id, created_at, updated_at, name, value, api)
VALUES ($1, $2, $3, $4, $5, $6)
RETURNING *;

-- name: GetHeaderByID :one
SELECT *
FROM header
WHERE id = $1;

-- name: ListHeader :many
SELECT *
FROM header;

-- name: GetHeaderByApi :many
SELECT *
FROM header
where api = $1;