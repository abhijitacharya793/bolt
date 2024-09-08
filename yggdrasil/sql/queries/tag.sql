-- name: CreateTag :one
INSERT INTO tag (id, created_at, updated_at, name)
VALUES ($1, $2, $3, $4)
RETURNING *;

-- name: GetTagByID :one
SELECT *
FROM tag
WHERE id = $1;

-- name: ListTag :many
SELECT *
FROM tag;

-- name: DeleteTag :exec
DELETE
FROM tag
WHERE id = $1;