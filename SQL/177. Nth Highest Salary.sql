CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select if(count(*)=N,min(salary),null)
      from(select distinct salary
            from employee
            order by salary desc limit N)a
      
      
      
      
  );
END
