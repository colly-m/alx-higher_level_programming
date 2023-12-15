-- Script to list all genres in a database 'hbtn_0d_tvshows_rate' by dating
-- Each record displaying 'tv_genres.name' - 'rating sum'

SELECT name, SUM(tv_show_rating.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
