def contient_e(chaine):
    return 'e' in chaine

chaine =input("Mot :")

if contient_e(chaine):
    print(f'Le mot "{chaine}" contient le caractère "e".')
else:
    print(f'Le mot "{chaine}" ne contient pas le caractère "e".')

