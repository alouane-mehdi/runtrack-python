def liste2(liste):
    lst = []
    for i in liste:
        if i not in lst:
            lst.append(i)
    return lst

liste_initiale = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

resultat = liste2(liste_initiale)

print(resultat)