-- Script that displays the max temperature of each state (ordered by State name).
SELECT state, value "max_temp" FROM temperatures WHERE value = (SELECT MAX(value) FROM temperatures) GROUP BY state;
