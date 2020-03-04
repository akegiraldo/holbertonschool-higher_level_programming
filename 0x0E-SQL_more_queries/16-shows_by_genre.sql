-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT t_s.title, t_g.name FROM tv_shows t_s LEFT OUTER JOIN tv_show_genres t_s_g ON t_s.id = t_s_g.show_id LEFT OUTER JOIN tv_genres t_g ON t_s_g.genre_id = t_g.id ORDER BY t_s.title, t_g.name;
