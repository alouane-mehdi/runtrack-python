def message(type, saison):
    if type == "fruits" and saison == "hiver":
        return "Orange, mandarine et kiwi"
    elif type == "fruits" and saison == "ete":
        return "Poire, fraise, cassis"
    elif type == "legume" and saison =="hiver":
        return "carotte, topinambour, endive"
    elif type == "legume" and saison =="ete":
        return "artichaut, aubergine,navet"

a=message("legume", "hiver")
print(a)