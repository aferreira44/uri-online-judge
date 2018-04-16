employee_id = int(input())
worked_hours = float(input())
price_hour = float(input())
salary = worked_hours * price_hour

print('NUMBER = ' + str(employee_id))
print('SALARY = U$ ' + format(salary, '.2f'))