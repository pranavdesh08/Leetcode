select if(count(*)=2,min(salary),null) SecondHighestSalary
from
(select distinct salary
from employee
order by salary desc
limit 2)a
