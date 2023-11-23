def time_to_text(d):
    h = d // 60
    m = d % 60
    print(d, "min =", h, "h", m, "min")

duree_en_minutes = 2000
time_to_text(duree_en_minutes)
