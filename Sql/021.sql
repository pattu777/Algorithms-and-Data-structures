SELECT DISTINCT product.maker, MAX(pc.price)
FROM product, pc
WHERE 	product.model = pc.model
GROUP BY product.maker