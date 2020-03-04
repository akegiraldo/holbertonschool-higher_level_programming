-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t_s.title FROM tv_shows t_s INNER JOIN tv_show_genres t_s_g ON t_s.id = t_s_g.show_id INNER JOIN tv_genres t_g ON t_s_g.genre_id = t_g.id WHERE t_g.name = 'Comedy' ORDER BY t_s.title;
