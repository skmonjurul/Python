--3. Display jobs where the minimum salary is less than salary of employee 105.
select *
from  jobs
where min_salary<(select salary from employees
where employee_id=105);