// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.20.0
// source: header.sql

package database

import (
	"context"
	"time"

	"github.com/google/uuid"
)

const createHeader = `-- name: CreateHeader :one
INSERT INTO header (id, created_at, updated_at, name, value, api)
VALUES ($1, $2, $3, $4, $5, $6)
RETURNING id, created_at, updated_at, name, value, api
`

type CreateHeaderParams struct {
	ID        uuid.UUID
	CreatedAt time.Time
	UpdatedAt time.Time
	Name      string
	Value     string
	Api       uuid.UUID
}

func (q *Queries) CreateHeader(ctx context.Context, arg CreateHeaderParams) (Header, error) {
	row := q.db.QueryRowContext(ctx, createHeader,
		arg.ID,
		arg.CreatedAt,
		arg.UpdatedAt,
		arg.Name,
		arg.Value,
		arg.Api,
	)
	var i Header
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Name,
		&i.Value,
		&i.Api,
	)
	return i, err
}

const getHeaderByApi = `-- name: GetHeaderByApi :many
SELECT id, created_at, updated_at, name, value, api
FROM header
where api = $1
`

func (q *Queries) GetHeaderByApi(ctx context.Context, api uuid.UUID) ([]Header, error) {
	rows, err := q.db.QueryContext(ctx, getHeaderByApi, api)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items []Header
	for rows.Next() {
		var i Header
		if err := rows.Scan(
			&i.ID,
			&i.CreatedAt,
			&i.UpdatedAt,
			&i.Name,
			&i.Value,
			&i.Api,
		); err != nil {
			return nil, err
		}
		items = append(items, i)
	}
	if err := rows.Close(); err != nil {
		return nil, err
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}

const getHeaderByID = `-- name: GetHeaderByID :one
SELECT id, created_at, updated_at, name, value, api
FROM header
WHERE id = $1
`

func (q *Queries) GetHeaderByID(ctx context.Context, id uuid.UUID) (Header, error) {
	row := q.db.QueryRowContext(ctx, getHeaderByID, id)
	var i Header
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Name,
		&i.Value,
		&i.Api,
	)
	return i, err
}

const listHeader = `-- name: ListHeader :many
SELECT id, created_at, updated_at, name, value, api
FROM header
`

func (q *Queries) ListHeader(ctx context.Context) ([]Header, error) {
	rows, err := q.db.QueryContext(ctx, listHeader)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items []Header
	for rows.Next() {
		var i Header
		if err := rows.Scan(
			&i.ID,
			&i.CreatedAt,
			&i.UpdatedAt,
			&i.Name,
			&i.Value,
			&i.Api,
		); err != nil {
			return nil, err
		}
		items = append(items, i)
	}
	if err := rows.Close(); err != nil {
		return nil, err
	}
	if err := rows.Err(); err != nil {
		return nil, err
	}
	return items, nil
}