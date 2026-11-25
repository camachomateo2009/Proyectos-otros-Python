ganancia_por_dia = 15
dias_de_trabajo = 6
semanas_trabajadas = 4
meses_de_trabajo=5
gasto_semana = 20
ganancias_mes = ganancia_por_dia * dias_de_trabajo * semanas_trabajadas 
ganancias_totales = ganancia_por_dia * dias_de_trabajo * semanas_trabajadas * meses_de_trabajo
print("en 1 mes de trabajo ganare", ganancias_mes, "en 5 meses ganare", ganancias_totales)
gasto_mes= gasto_semana * semanas_trabajadas
restante_5_meses = ganancias_totales - gasto_mes * 5
total_por_semana = ganancia_por_dia * dias_de_trabajo - gasto_semana
print("a la semana me queda un total de", total_por_semana, "y a los 5 meses me queda", restante_5_meses)