def Taille(a):
    total=0
    for i in a:
        total+=1
    return total
def mini(a):
    Min,cpt=a[0],0
    R=0
    for i in a: 
        cpt=cpt+1
        if i < Min:
            Min=i
            R=cpt-1
    return Min, R

New_liste=[]
t=[10, 15, 20, 8, 69]


for i in range(Taille(t)):
    
    Min, R=mini(t)
    
    New_liste.append(Min)
    t.pop(R)
print(New_liste)
