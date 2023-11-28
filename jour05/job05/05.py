def messagecodé(message, decalage):
    resultat = ""

    for a in message:
        if a.isalpha():
            code_ascii = ord(a.lower())
            nouveau_code_ascii = (code_ascii - ord('a') + decalage) % 26 + ord('a')
            resultat += chr(nouveau_code_ascii)
        else:
            resultat += a
            
    return resultat

messageoriginal = "Allez sur le flanc droit"
decalage = 3
chiffrement = messagecodé(messageoriginal, decalage)

print(chiffrement)
