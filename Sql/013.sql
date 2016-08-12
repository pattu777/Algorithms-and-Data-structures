Technique 1:
============
SELECT AVG(PC.speed)
FROM PC, Product
WHERE PC.model=Product.model and Product.maker='A';


Technique 2:
============
SELECT AVG(PC.speed)
FROM PC
INNER JOIN Product
ON PC.model=Product.model
WHERE Product.maker='A'
