-- name: CreateQuery :one
INSERT INTO query (id, created_at, updated_at, name, value, api)
VALUES ($1, $2, $3, $4, $5, $6)
RETURNING *;

-- name: GetQueryByID :one
SELECT *
FROM query
WHERE id = $1;

-- name: ListQuery :many
SELECT *
FROM query;

-- name: GetQueryByApi :many
SELECT *
FROM query
where api = $1;