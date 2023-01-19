USE EMP_TABLE;

-- Write a query that returns the Employees first name as upper case using an alias

-- SELECT UPPER(emptable1.Employee_Fname) AS UPPERCASE_FIRST FROM emptable1

-- Write a query to return the number of employees employed in software engineering departmentt
-- SELECT COUNT(*) FROM emptable1 WHERE Deparment = 'Software Engineer';

-- Write q query to find all the employees whose salary is between 50000 to 100000
-- FROM emptable2
--  WHERE Salary BETWEEN '50000' AND '100000'

-- Write a query to find the names of employees that begin with ‘S’
-- SELECT * 
-- FROM emptable1
-- WHERE Employee_Fname LIKE 'S%'

-- Write a query to retrieve the EmpFname and EmpLname in a single column as “FullName”. 
-- The first name and the last name must be separated with space

-- SELECT concat(Employee_Fname, " ", Employee_Lname) 
-- as Employee_Full FROM emptable1

-- Write a query find the total number of employees whose DOB is between 01/01/1990 to 12/31/1985 
-- and are grouped through gender

-- SELECT Count(*) as NUMBER_OF_EMP, Gender FROM emptable1
--  WHERE DOB BETWEEN '01/01/1980 ' AND '12/31/1985' 
-- GROUP BY Gender;

-- Write a query to fetch all employees who also hold the EXECUTIVE position.
-- SELECT E1.Employee_Fname, E1.Employee_Lname, E2.Position, E2.Salary, E1.Deparment
-- FROM emptable1 E1 Inner Join emptable2 E2
-- On E1.Employee_ID = E2.Employee_ID and E2.Position = 'EXECUTIVE'; 
 
-- Write a query to fetch the department-wise count of employees sorted by 
-- department’s count in ascending order
-- SELECT Deparment, count(Employee_ID) AS EmpDeptCount 
-- FROM emptable1 GROUP BY Deparment 
-- ORDER BY EmpDeptCount ASC;

-- Write a query to retrieve the sum of each salaries' position 
-- SELECT E2.Position, SUM(E2.Salary) as SumSalaries_of_Position
-- from emptable2 as E2
-- GROUP BY E2.Position;





