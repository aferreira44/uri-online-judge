def mean(numbers, weights):
  return float(sum(numbers)) / sum(weights)

a = float(input())
a_weight = 2

b = float(input())
b_weight = 3

c = float(input())
c_weight = 5

MEDIA = mean([a * a_weight, b * b_weight, c * c_weight], [a_weight, b_weight, c_weight])

print('MEDIA = ' + format(MEDIA, '.1f'))