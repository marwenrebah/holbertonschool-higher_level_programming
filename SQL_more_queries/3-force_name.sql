-- Script that creates the table force_name on my MySQL server.
CREATE table IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);