// Code generated by sqlc. DO NOT EDIT.
// versions:
//   sqlc v1.20.0
// source: burp_export.sql

package database

import (
	"context"
	"time"

	"github.com/google/uuid"
)

const createBurpExport = `-- name: CreateBurpExport :one
INSERT INTO burp_export (id, created_at, updated_at, name, scope, power, burpExport)
VALUES ($1, $2, $3, $4, $5, $6, $7)
RETURNING id, created_at, updated_at, name, scope, power, burpexport
`

type CreateBurpExportParams struct {
	ID         uuid.UUID
	CreatedAt  time.Time
	UpdatedAt  time.Time
	Name       string
	Scope      string
	Power      string
	Burpexport string
}

func (q *Queries) CreateBurpExport(ctx context.Context, arg CreateBurpExportParams) (BurpExport, error) {
	row := q.db.QueryRowContext(ctx, createBurpExport,
		arg.ID,
		arg.CreatedAt,
		arg.UpdatedAt,
		arg.Name,
		arg.Scope,
		arg.Power,
		arg.Burpexport,
	)
	var i BurpExport
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Name,
		&i.Scope,
		&i.Power,
		&i.Burpexport,
	)
	return i, err
}

const deleteBurpExport = `-- name: DeleteBurpExport :exec
DELETE
FROM burp_export
WHERE id = $1
`

func (q *Queries) DeleteBurpExport(ctx context.Context, id uuid.UUID) error {
	_, err := q.db.ExecContext(ctx, deleteBurpExport, id)
	return err
}

const getBurpExportByID = `-- name: GetBurpExportByID :one
SELECT id, created_at, updated_at, name, scope, power, burpexport
FROM burp_export
WHERE id = $1
`

func (q *Queries) GetBurpExportByID(ctx context.Context, id uuid.UUID) (BurpExport, error) {
	row := q.db.QueryRowContext(ctx, getBurpExportByID, id)
	var i BurpExport
	err := row.Scan(
		&i.ID,
		&i.CreatedAt,
		&i.UpdatedAt,
		&i.Name,
		&i.Scope,
		&i.Power,
		&i.Burpexport,
	)
	return i, err
}

const listBurpExport = `-- name: ListBurpExport :many
SELECT id, created_at, updated_at, name, scope, power, burpexport
FROM burp_export
`

func (q *Queries) ListBurpExport(ctx context.Context) ([]BurpExport, error) {
	rows, err := q.db.QueryContext(ctx, listBurpExport)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	var items []BurpExport
	for rows.Next() {
		var i BurpExport
		if err := rows.Scan(
			&i.ID,
			&i.CreatedAt,
			&i.UpdatedAt,
			&i.Name,
			&i.Scope,
			&i.Power,
			&i.Burpexport,
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
