CREATE TABLE IF NOT EXISTS modified_film (
    film_id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    release_year INTEGER,
    language_id INTEGER,
    rental_duration INTEGER,
    rental_rate NUMERIC,
    length INTEGER,
    replacement_cost NUMERIC,
    rating VARCHAR(10),
    last_update TIMESTAMP,
    special_features TEXT[],
    fulltext TSVECTOR,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
