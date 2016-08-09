Solution 1:
===========
SELECT DISTINCT Product.maker
FROM Product, PC
WHERE PC.speed >= 450 AND Product.model=PC.model;

Solution 2:
===========
SELECT DISTINCT Product.maker
FROM Product JOIN PC
ON Product.model=PC.model
WHERE PC.speed >= 450;

Solution 3:
===========
SELECT maker
FROM product
JOIN pc ON product.model = pc.model
WHERE pc.speed >= 450
GROUP BY product.maker;
