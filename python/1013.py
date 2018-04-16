nums = input().split()

for i, n in enumerate(nums):
  nums[i] = int(n)

print(str(max(nums)) + ' eh o maior')