N = []

# Read input
for x in range(20):
  N.append(int(input()))

# Swap arr[0] with arr[19], arr[1] with arr[18] and so on..
for i in range(int(len(N)/2)):
  j = len(N)-1-i
  temp = N[i]
  N[i] = N[j]
  N[j] = temp

# Print changed array
for i, n in enumerate(N):
  print('N[' + str(i) + '] = ' + str(n))