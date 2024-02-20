-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT tv_genres.name AS genre, tv_shows.id
FROM tv_genres
LEFT JOIN tv_shows ON tv_shows.id = tv_genres.id
ORDER BY tv_shows.id DESC;
