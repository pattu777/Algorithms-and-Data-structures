SELECT maker FROM Product WHERE type='PC'
EXCEPT
SELECT maker FROM Product WHERE type='Laptop'
