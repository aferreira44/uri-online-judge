class Product():
  def __init__(self, args):
    self.id = int(args[0])
    self.number_units = float(args[1])
    self.unit_price = float(args[2])

  def subtotal(self):
    return self.number_units * self.unit_price

product_1 = Product(input().split())
product_2 = Product(input().split())

total = sum([product_1.subtotal(), product_2.subtotal()])

print('VALOR A PAGAR: R$ ' + format(total, '.2f'))