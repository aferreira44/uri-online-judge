def mean(numbers, weights):
  return float(sum(numbers)) / sum(weights)

a = float(input())
a_weight = 3.5

b = float(input())
b_weight = 7.5

MEDIA = mean([a * a_weight, b * b_weight], [a_weight, b_weight])

print('MEDIA = ' + format(MEDIA, '.5f'))