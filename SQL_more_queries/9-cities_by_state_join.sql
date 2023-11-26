-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT C.id, C.name, S.name
FROM cities C
INNER JOIN States S
ON C.state_id = S.id
ORDER BY C.id ASC;