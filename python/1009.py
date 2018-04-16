seller_name = input()
fixed_salary = float(input())
seller_sales = float(input())

bonus = seller_sales * 0.15
final_salary = fixed_salary + bonus

print('TOTAL = R$ ' + format(final_salary, '.2f'))
