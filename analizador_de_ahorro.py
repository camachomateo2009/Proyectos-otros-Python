def analizador_de_ahorro():
    dinero_actual=float(input("¿cuánto dinero tiene actualmente? "))
    ahorro_semanal=float(input("¿cuánto ahorras cada semana? "))
    meta_ahorro=float(input("¿cuál es tu meta de ahorro? "))
    ahorro_total=dinero_actual+ahorro_semanal
    semanas=1
    while ahorro_total<meta_ahorro:
        semanas=semanas+1
        ahorro_total=ahorro_total+ahorro_semanal

    if semanas<=4:
        tiempo= semanas
        unidad="semanas"
    elif semanas<52:
        tiempo=semanas/4
        unidad="meses"
    else:
        tiempo=semanas/52
        unidad="años"
    print(f"OK, Si tu meta de ahorro de {meta_ahorro:,.2f} se cumplira en {tiempo:.2f} {unidad} ahorrando tus {ahorro_semanal:,.2f} semanales.")
analizador_de_ahorro()