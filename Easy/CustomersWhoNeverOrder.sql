# Ref from: https://leetcode.com/problems/customers-who-never-order/solutions/3202156/to-the-point-solution-without-join/
SELECT name AS Customers
FROM Customers
WHERE id not in (
    SELECT customerID
    FROM Orders
);