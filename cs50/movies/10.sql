SELECT DISTINCT(name) FROM people
WHERE id IN (SELECT person_id FROM directors
WHERE movie_id IN (SELECT movie_id FROM ratings
WHERE rating >= 9.0));

SELECT DISTINCT(name) FROM people
JOIN directors
ON id = person_id
JOIN ratings
ON directors.movie_id = ratings.movie_id
WHERE rating >= 9.0;