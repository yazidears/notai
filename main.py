print("notAI")
print("made by yazidears, maaarinaaa and ")
print("check it out on https://github.com/yazidears/notai")
print("Importing data, please wait.")
import os
import time
import functions
import random
import sys
import json
import requests
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
print("Imported data.")
print("Welcome to notAI!")
print("Who are you, what's your name?")
name = input("->")
print("Welcome, " + name )
time.sleep(2)
clear()
print("Usando este programa aceptas los Terminos de dichos servicios usados.")
print("Using this program you accept the Terms of the services used.")
time.sleep(1)
clear()
print("Menu")
print("1. Clasificacion de imagenes")
print("2. Procesamiento de lenguaje natural")
print("3. Recomendaciones")
print("4. Reconocimiento de voz")
print("5. Prediccion de percios")
print("6. Analisis de sentimientos")
print("7. Deteccion de fraudes")
print("---------------------------------")
print("Menu de limitaciones")
print("9. Chat con presets")
print("--------------------------------")
print("Selección:")
sel = input("->")
if sel in "123456789":
    print("Cargado...")
    uwu = open("sel.uwu", "x")
    uwu.write(sel)
    uwu.close()
    print("Escribiendo datos...")
    uwu = open("name.uwu", "x")
    uwu.write(name)
    uwu.close()
    print("Ejecutando...")
    os.system("python3 functions.py")