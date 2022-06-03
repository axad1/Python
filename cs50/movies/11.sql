SELECT title FROM movies JOIN ratings
ON id = movie_id
WHERE id IN (SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people
WHERE name = "Chadwick Boseman"))
ORDER BY rating DESC
LIMIT 5;


SELECT title FROM movies
JOIN stars
ON movies.id = stars.movie_id
JOIN people ON
person_id = people.id
JOIN ratings ON
movies.id = ratings.movie_id
WHERE name = 'Chadwick Boseman'
ORDER BY rating DESC
LIMIT 5;