import threading
import time
import keyboard

bucle = True
pause = False

def sensor(texto, delay):
    count = 0
    global bucle
    global pause
    while bucle:
        if not pause:
            time.sleep(delay)
            count+=delay
            impresion= str(texto)+"   INDICE    "+str(count/delay)+"\n"
            print(impresion)

def interruptor():
    global bucle
    global pause
    while bucle:
        if keyboard.read_key() == "b":
            break
        elif keyboard.read_key() == "p":
            pause= not pause
            print("Sistema pausado/reanudado.")
    bucle=False
    
            

t1 = threading.Thread(target=sensor, args=('sensor1', 1))
t2 = threading.Thread(target=sensor, args=('sensor2', 2))
t3 = threading.Thread(target=sensor, args=('sensor3', 4))
t4 = threading.Thread(target=interruptor)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("ejecucion finalizada.")


"""Imaginemos una aplicación que mide el estado de tres sensores. Suponiendo
que cada sensor necesita medirse a una frecuencia diferente, es decir, uno
cada 1 segundos, otro cada 2 segundos y un tercero cada 4 segundos.
Escriba un programa que lea los tres sensores durante 1 minuto."""
