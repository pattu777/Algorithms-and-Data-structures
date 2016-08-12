Technique 1:
============
SELECT DISTINCT 'Laptop' AS type, model, speed
FROM Laptop
WHERE speed <
  (SELECT MIN(speed) FROM PC)


Technique 2:
============
SELECT DISTINCT 'Laptop' AS type, model, speed
FROM Laptop
WHERE speed <
  ALL (SELECT speed FROM PC)
