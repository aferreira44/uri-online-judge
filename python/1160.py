T = int(input())

for i in range(T):
  Pa, Pb, Ga, Gb = input().split()
  Pa = int(Pa)
  Pb = int(Pb)
  Ga = float(Ga.format('.1f'))
  Gb = float(Gb.format('.1f'))
  years = 0

  paDEF = Pa
  pbDEF = Pb

  while Pa <= Pb:
    Pa += Pa * (Ga / 100)
    Pb += Pb * (Gb / 100)
    years += 1

    if (years > 100):
      print('Mais de 1 seculo.')
      break
  else:
    print(str(years) + ' anos.')