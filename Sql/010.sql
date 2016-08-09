SELECT model, price
FROM Printer
WHERE Printer.price=
  (SELECT MAX(price)
  FROM Printer)
