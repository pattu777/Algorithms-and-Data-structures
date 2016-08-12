Technique 1:
============
SELECT Product.maker, AVG(Laptop.screen)
FROM Product
INNER JOIN Laptop
ON Product.model=Laptop.model
GROUP BY Product.maker


Technique 2:
============
SELECT Product.maker, AVG(Laptop.screen)
FROM Product, Laptop
WHERE Product.model=Laptop.model
GROUP BY Product.maker
