-- +goose Up
CREATE TABLE enricher
(
    id         UUID PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    api_id     UUID      NOT NULL,
    scan_id    UUID      NOT NULL,
    scan_name  TEXT      NOT NULL,
    power      TEXT      NOT NULL,
    scope      TEXT      NOT NULL,
    tasks      TEXT      NOT NULL,
    completion TEXT      NOT NULL,
    status     TEXT      NOT NULL
);

-- +goose Down
DROP TABLE enricher;

