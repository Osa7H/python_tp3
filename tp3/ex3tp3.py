def conversion_temps(h, m, s):

  if h < 0 or h > 23:
    print("Le nombre d'heures doit être compris entre 0 et 23.")
  if m < 0 or m > 59:
    print("Le nombre de minutes doit être compris entre 0 et 59.")
  if s < 0 or s > 59:
    print("Le nombre de secondes doit être compris entre 0 et 59.")

  return 3600 * h + 60 * m + s


print(conversion_temps(12, 34, 56) ,"s")