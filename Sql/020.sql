SELECT maker, COUNT(1)
FROM Product
WHERE type='PC'
GROUP BY maker
HAVING COUNT(1) >= 3
