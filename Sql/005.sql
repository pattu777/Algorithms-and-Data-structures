SELECT model, speed, hd
FROM PC
WHERE price < 600 AND (cd='12x' or cd='24x');
