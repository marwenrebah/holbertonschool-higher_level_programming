-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT C.id, C.name, S.name AS state
FROM cities c
JOIN states s ON C.state_id = S.id
ORDER BY C.id ASC;