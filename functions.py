print("Functions")
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()
ca = open("sel.uwu", "r")
sel = ca.read()
ca.close()
ca = open("name.uwu", "r")
name = ca.read()
ca.close()
if sel == "1":
    print("Clasificacion de imagenes")
    os.system("python3 img.py")
elif sel == "2":
    print("Procesamiento de lenguaje natural")
elif sel == "3":
    print("Recomendaciones")
elif sel == "4":
    print("Reconocimiento de voz")
    os.system("python3 recognise.py")
elif sel == "5":
    print("Prediccion de precios")  
elif sel == "6":
    print("Analisis de sentimientos")
elif sel == "7":
    print("Deteccion de fraudes")
elif sel == "8":
    print("Chat con presets")