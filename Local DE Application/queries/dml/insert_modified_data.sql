INSERT INTO modified_film (
    film_id, title, description, release_year, language_id,
    rental_duration, rental_rate, length, replacement_cost,
    rating, last_update, special_features, fulltext
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (film_id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    release_year = EXCLUDED.release_year,
    language_id = EXCLUDED.language_id,
    rental_duration = EXCLUDED.rental_duration,
    rental_rate = EXCLUDED.rental_rate,
    length = EXCLUDED.length,
    replacement_cost = EXCLUDED.replacement_cost,
    rating = EXCLUDED.rating,
    last_update = EXCLUDED.last_update,
    special_features = EXCLUDED.special_features,
    fulltext = EXCLUDED.fulltext,
    modified = CURRENT_TIMESTAMP;
