def time_to_text(d):
    h = d // 60
    m = d % 60
    s = m % 60
    print(d, "min =", h, "h", m, "min", s, "s")

duree_en_minutes = 1585
time_to_text(duree_en_minutes)
