SELECT DISTINCT first.email AS Email
FROM Person AS first
JOIN Person AS second
ON first.email = second.email 
where first.id != second.id AND first.email = second.email