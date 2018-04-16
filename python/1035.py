nums = input().split()

def is_accepted(a, b, c, d):
  if (b > c and d > a and sum([c, d]) > sum([a, b]) and c > 0 and d > 0 and a % 2 == 0):
    return True
  else:
    return False

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])

print('Valores aceitos' if is_accepted(a, b, c, d) else 'Valores nao aceitos')