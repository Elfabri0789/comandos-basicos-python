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


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(ahora)
print_date(year_2025)

from datetime import date    #ACCEDEMOS A MODULO#

current_time= date.today()

print(current_time.year)
print(current_time.month)
print(current_time.day)

diff= year_2025 - ahora  #hacemos la funcion para saber cuanto queda hasta el nuevo año
print(diff)

from datetime import timedelta    #ACCEDEMOS A MODULO#

time_delta= timedelta()