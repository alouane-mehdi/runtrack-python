nom = 'bouteille'
prix = 10
quantite = 50

print(nom, prix, quantite)

quantite_achetee = int(input("Combien de bouteilles voulez-vous acheter ?"))

if quantite_achetee <= quantite:
    quantite -= quantite_achetee
    prix *= 1.1  

    print(f"Achat réussi ! Stock mis à jour. Nouveau stock : {quantite}")
    print(f"Prix mis à jour après inflation : {prix}")
    print(nom, prix , quantite)
else:
    print("Désolé, stock insuffisant.")

rajout_stock = int(input("Combien voulez-vous rajouter de stock ?"))

quantite += rajout_stock
print(f"Mise à jour du stock réussie. Nouveau stock : {quantite}")




