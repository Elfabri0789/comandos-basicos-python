
#LOOPS O BUCLES /CICLOS #
# LOS BUCLES NOS SIRVEN PARA ITERAR, ES DECIR PASAR VARIAS VECES POR EL CODIGO

my_condicion= 0             #un codigo asi haria que el sistema entre en un bucle, hasta explortar la compu.
                            # el while, revisa la condicion, y solo se detiene si la condicion no se cumple. al cumplir
while my_condicion < 10:     # y no cambiar, entra en un bucle infinito. a lo que hay que agregarle otra condicion
    print(my_condicion)

    my_condicion += 2 # solo aca, no habra un bucle infinito. ya que va agregando de 2 en 2, hasta que  # la condicion deje de cumplirse
else:         # el else es compatible con el while, pero tambien es opcional             
     print(" la condicion es mayor o igual a 10")               


my_condicionn= 0

while my_condicionn < 20:
    my_condicionn += 1
    if my_condicionn == 13:
        print("se detendra la ejecucion, pero seguira") # aca la ejecucion se detendra, pero seguira
        break # con el breack cortamos en seco la ejecucion, por mas que la condicion, se siga cumpliendo
    print(my_condicionn) 


# BUCLE FOR: for se ejecuta! tantas veces, como elementos tengamos. una vez, por cada elemento que tengamos.

my_list= [23, 45, 65, 32, 90, 35, 23]

for element in my_list:
    print(element)


mi_tupla= ("fabri", "fernandez", 35, 1989)
for tupla in mi_tupla:
    print(tupla)


my_dict={"nombre": "fabricio",
        "Apellido": "Fernandez",
        "Edad": 35,
        "idiomas": {"html", "python", "javascrip"} #un set dentro de un dict
        }

for dict in my_dict: 
    print(dict) # en el caso de los dict, nos imprime los keys, no los values

my_dict={"nombre": "fabricio",
        "apellido": "Fernandez",
        "edad": 35,
        "idiomas": {"html", "python", "javascrip"} #un set dentro de un dict
        }

for dict in my_dict: 
    print(dict) # en el caso de los dict, nos imprime los keys, no los values
    if dict== "edad":
        break
print("ejecuto, hasta que el brack lo corto en el valor : edad, dejando fuera, a idiomas")


for dict in my_dict: 
    print(dict) # en el caso de los dict, nos imprime los keys, no los values
    if dict== "apellido":
        continue # con continue, el saltea el "apellido" y sigue 
print("ejecuto, por mas que le pasaramos el if")
