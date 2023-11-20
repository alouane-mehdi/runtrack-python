montant_initial = float(input("Entrez le montant initial de l'investissement : "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel en pourcentage : "))

gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel} euros")

montant_initial += 5000
taux_rendement_annuel += 2

nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel : {nouveau_gain_annuel} euros")

retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

montant_final = montant_initial + nouveau_gain_annuel
print(f"Montant final de l'investissement : {montant_final} euros")

