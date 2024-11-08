##DATES##

from datetime import datetime    #ACCEDEMOS A MODULO#

ahora = datetime.now() #creamos objeto, accedemos a datetime. now, es una palabra reservada 

print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)

timestamp= ahora.timestamp() #TIMESTAMP ES UNA PALABRA RESERVADA Y SIGNIFICA EN ESTE MOMENTO EN EL TIEMPO DESDE LA CREACION#

print(timestamp)

year_2025= datetime(2025,1,1)