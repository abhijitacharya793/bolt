-- +goose Up
CREATE TABLE header
(
    id         UUID PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    name       TEXT      NOT NULL,
    value      TEXT      NOT NULL,
    api        UUID      NOT NULL REFERENCES api (id) ON DELETE CASCADE
);

-- +goose Down
DROP TABLE header;