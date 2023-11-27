def arrondi(nombre):
    décimaux = nombre - int(nombre)
    if décimaux >= 0.5:
        return int(nombre) + 1
    else:
        return int(nombre)

def tri(arr):
    tri_arr = []
    while arr:
        min_element = min(arr)
        tri_arr.append(min_element)
        arr.remove(min_element)
    return tri_arr

numeros = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

numeros_arrondi = [arrondi(num) for num in numeros]
numeros_arrondis_triés = tri(numeros_arrondi)



print( numeros_arrondis_triés)
