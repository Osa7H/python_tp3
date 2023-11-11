def somme(m, n):
  if m > n:
    print("m doit être inférieur ou égal à n.")
  somme = 0
  for i in range(m, n + 1):
    somme += i
  return somme

print(somme(2,5))