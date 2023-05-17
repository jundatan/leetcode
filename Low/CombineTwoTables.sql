# Write your MySQL query statement below
SELECT person.firstName, person.lastName, address.city, address.state
FROM Person as person
LEFT JOIN Address as address
ON Person.personId = Address.personId;