-- +goose Up
CREATE TABLE tag
(
    id         UUID PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    name       TEXT      NOT NULL
);
CREATE TABLE fuzzing
(
    id         UUID PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    part       TEXT      NOT NULL,
    condition  TEXT      NOT NULL,
    required   TEXT      NOT NULL
);
CREATE TABLE risk
(
    id           UUID PRIMARY KEY,
    created_at   TIMESTAMP NOT NULL,
    updated_at   TIMESTAMP NOT NULL,
    name         TEXT      NOT NULL,
    abbreviation TEXT      NOT NULL,
    description  TEXT      NOT NULL,
    remediation  TEXT      NOT NULL
);
CREATE TABLE vulnerability
(
    id                 UUID PRIMARY KEY,
    created_at         TIMESTAMP NOT NULL,
    updated_at         TIMESTAMP NOT NULL,
    name               TEXT      NOT NULL,
    risk               UUID      NOT NULL REFERENCES risk (id) ON DELETE CASCADE,
    command            TEXT      NOT NULL,
    severity           TEXT      NOT NULL,
    steps_to_reproduce TEXT      NOT NULL,
    power              TEXT      NOT NULL
);
CREATE TABLE vulnerability_tag
(
    id               UUID PRIMARY KEY,
    vulnerability_id UUID NOT NULL REFERENCES vulnerability (id) ON DELETE CASCADE,
    tag_id           UUID NOT NULL REFERENCES tag (id) ON DELETE CASCADE,
    CONSTRAINT unique_vulnerability_tag UNIQUE (vulnerability_id, tag_id)
);
CREATE TABLE vulnerability_fuzzing
(
    id               UUID PRIMARY KEY,
    vulnerability_id UUID NOT NULL REFERENCES vulnerability (id) ON DELETE CASCADE,
    fuzzing_id       UUID NOT NULL REFERENCES fuzzing (id) ON DELETE CASCADE,
    CONSTRAINT unique_vulnerability_fuzzing UNIQUE (vulnerability_id, fuzzing_id)
);
CREATE TABLE template
(
    id            UUID PRIMARY KEY,
    created_at    TIMESTAMP NOT NULL,
    updated_at    TIMESTAMP NOT NULL,
    vulnerability UUID      NOT NULL REFERENCES vulnerability (id) ON DELETE CASCADE,
    path          TEXT      NOT NULL
);

-- +goose Down
DROP TABLE tag;
DROP TABLE fuzzing;
DROP TABLE risk;
DROP TABLE vulnerability;
DROP TABLE vulnerability_tag
DROP TABLE vulnerability_fuzzing;
DROP TABLE template;