
def moyenne(a, b, c):
    return (a + b + c) / 3

a=int(input("Quelle est votre note"))
b=int(input("Quelle est votre note"))
c=int(input("Quelle est votre note"))

moyenne_etudiant=moyenne(a, b, c)

print(moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20 :
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14 :
    print("Bon élève")   
elif 8 <= moyenne_etudiant <= 10 :
    print("Eleve moyen") 
elif 0 <= moyenne_etudiant <= 7 :
    print("Élève devant faire des efforts")       
    
    


    
    