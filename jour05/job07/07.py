notes=int(input("Quelle est votre note?"))

if notes < 40 :
    print("Tu as échoué au test")

elif notes > 40 :
    print("Tu as réussi le test")
    
       
def arr(note):
    prochainmultiplede5 = (note // 5 + 1) * 5
    if prochainmultiplede5 - note < 3:
        return prochainmultiplede5
    else:
        return note

print(arr(notes))