import math


def delta(a, b, c):

  return b ** 2 - 4 * a * c


def nombre_racines(a, b, c):

  if delta(a, b, c) > 0:
    return 2
  elif delta(a, b, c) == 0:
    return 1
  else:
    return 0


def affiche_nombre_racines(a, b, c):

  print("L'équation a ",nombre_racines(a, b, c)," solution(s).", )


def racine1(a, b, c):

  return (-b + math.sqrt(delta(a, b, c))) / (2 * a)


def racine2(a, b, c):

  return (-b - math.sqrt(delta(a, b, c))) / (2 * a)


print(delta(1, 2, 1))
print(nombre_racines(1, 2, 1))
affiche_nombre_racines(1, 2, 1)
print(racine1(1, 2, 1))
print(racine2(1, 2, 1))