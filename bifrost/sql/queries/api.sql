-- name: CreateApi :one
INSERT INTO api (id, created_at, updated_at, target, root_domain, domain, protocol, protocol_version, port, method,
                 path, body)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)
RETURNING *;

-- name: GetApiByID :one
SELECT *
FROM api
WHERE id = $1;

-- name: ListApi :many
SELECT *
FROM api;

-- name: DeleteApi :exec
DELETE
FROM api
WHERE id = $1;