-- name: CreateTemplate :one
INSERT INTO template (id, created_at, updated_at, vulnerability, path)
VALUES ($1, $2, $3, $4, $5)
RETURNING *;

-- name: GetTemplateByID :one
SELECT *
FROM template
WHERE id = $1;

-- name: ListTemplate :many
SELECT *
FROM template;

-- name: DeleteTemplate :exec
DELETE
FROM template
WHERE id = $1;