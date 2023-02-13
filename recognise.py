import speech_recognition as sr
import time
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
from sender import *
# Inicializar el reconocedor de voz
r = sr.Recognizer()

# Inicializar el micrófono
mic = sr.Microphone()
send("Iniciando")
# Función para detener la grabación automáticamente después de 30 segundos
def stop_listening(recognizer, elapsed_time, max_time):
    if elapsed_time > max_time:
        return True
    return False
send("Reconociendo")
print("Di algo:")

# Escuchar la entrada del micrófono hasta que se detenga automáticamente después de 30 segundos
with mic as source:
    audio = r.listen(source, phrase_time_limit=30, timeout=30)
# Reconocer la voz en el audio y mostrar el texto reconocido en tiempo real
text = r.recognize_google(audio, language = "es-ES")
clear()
words = text.split()
palabras = len(words)
palabras = str(palabras)
send("'"+text+"' reconocido, "+palabras+" palabras")
print("Datos enviados.")
if os.path.exists("sel.uwu"):
    xd = open("sel.uwu","w")
    xd.write("returnfrom 4")
    xd.close()
    
