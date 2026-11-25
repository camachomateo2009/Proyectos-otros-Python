pregunta=input("¿Qué juegos quieres buscar?")
juegos=["Clash Royale", "God of War", "GTA 6", "RDR2", "Cuphead"]
juegos[4]="MINECRAFT"
juegos.append("Roblox")
if(pregunta in juegos):
    print("!!esta disponible este juego!!")
else:
    print("no lo tienes")
PREGUNTA=input("¿Adivina cuantos juegos tienes?")
print(len(juegos))
PREGUNTAA=input("¿Quieres saber tus juegos ? si o no")
if(PREGUNTAA=="si"):
    print(juegos)
else:
    print("OK")