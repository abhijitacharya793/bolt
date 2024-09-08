-- +goose Up
CREATE TABLE api
(
    id               UUID PRIMARY KEY,
    created_at       TIMESTAMP NOT NULL,
    updated_at       TIMESTAMP NOT NULL,
    target           TEXT      NOT NULL,
    root_domain      TEXT      NOT NULL,
    domain           TEXT      NOT NULL,
    protocol         TEXT      NOT NULL,
    protocol_version TEXT      NOT NULL,
    port             TEXT      NOT NULL,
    method           TEXT      NOT NULL,
    path             TEXT      NOT NULL,
    body             TEXT      NOT NULL
);

-- +goose Down
DROP TABLE api;