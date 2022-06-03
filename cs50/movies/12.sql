SELECT title FROM movies
WHERE id IN (SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people
WHERE name = "Johnny Depp"))
INTERSECT
SELECT title FROM movies
WHERE id IN (SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people
WHERE name = "Helena Bonham Carter"));


SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Johnny Depp" AND title IN
(SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Helena Bonham Carter");










