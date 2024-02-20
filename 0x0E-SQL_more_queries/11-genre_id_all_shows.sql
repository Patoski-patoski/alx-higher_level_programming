--  a script that lists all shows contained in the database hbtn_0d_tvshows

SELECT tv_shows.title, tv_show_genres.show_id
FROM tv_shows
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id or NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
