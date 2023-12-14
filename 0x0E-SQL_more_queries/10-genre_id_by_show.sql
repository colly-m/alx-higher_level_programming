-- Script to list all shows in a adatabase dump that have at least one genre linked

SELECT tv_shows.tittle, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
