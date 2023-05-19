SELECT employee.name AS Employee
FROM Employee AS employee
LEFT JOIN Employee AS manager
ON employee.managerId = manager.id
WHERE employee.salary > manager.salary