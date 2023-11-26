-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities C
INNER JOIN states S
ON C.state_id = states.name
ORDER BY cities.id ASC;