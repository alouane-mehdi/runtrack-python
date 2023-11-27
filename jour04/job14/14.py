def Taille(a):
    total=0
    for i in a:
        total+=1
    return total
        
liste1=[]
liste2=[]

def my_long_word(nombre,chaine):
    liste=chaine.split()
    for i in liste:
        if i!= ",":
            liste2.append(i)
    for i in liste2:
        if Taille(i) > nombre:
            liste1.append(i)
            
        
             
    print(liste1)


my_long_word(3,"La peur est le chemin vers le côté obscur , la peur mène à la colère , la colère mène à la haine , la haine mène à la souffrance")