-- Script that displays the max temperature of each state (ordered by State name).
SELECT state, max(value) "max_temp" from temperatures GROUP BY state ORDER BY state ASC;
