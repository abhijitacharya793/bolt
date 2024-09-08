-- +goose Up
CREATE TABLE burp_export
(
    id         UUID PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    name       TEXT      NOT NULL,
    scope      TEXT      NOT NULL,
    power      TEXT      NOT NULL,
    burpExport TEXT      NOT NULL
);

-- +goose Down
DROP TABLE burp_export;