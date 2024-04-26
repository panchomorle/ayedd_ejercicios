import threading
import time

"""Imaginemos una aplicación que mide el estado de tres sensores. Suponiendo
que cada sensor necesita medirse a una frecuencia diferente, es decir, uno
cada 1 segundos, otro cada 2 segundos y un tercero cada 4 segundos.
Escriba un programa que lea los tres sensores durante 1 minuto."""

def sensor(texto, delay):
    count = 0
    while count < 60:
        time.sleep(delay)
        count+=delay
        print(texto,"   INDICE    ",count/delay)
        

t1 = threading.Thread(target=sensor, args=('sensor1', 1))
t2 = threading.Thread(target=sensor, args=('sensor2', 2))
t3 = threading.Thread(target=sensor, args=('sensor3', 4))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("ejecucion finalizada.")
