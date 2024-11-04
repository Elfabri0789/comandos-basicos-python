# DICTIONARIES #
# el sirve para armar una estructura de datos de tipo clave valor, separado de un :
# en javascrip, seria como un Json

my_dict= dict()
my_other_dict= {}

print(type(my_dict))

my_other_dict={"nombre": "fabricio", "Apellido": "Fernandez", "Edad": 35} #el dict lo formamos con clave valor, separado de un :
print(my_other_dict)

my_dict={"nombre": "fabricio",
        "Apellido": "Fernandez",
        "Edad": 35,
        "idiomas": {"html", "python", "javascrip"} #un set dentro de un dict
        }

print(my_dict)

print(my_dict["Edad"]) # asi accedemos a un elemento
my_dict["Edad"]= 34 # asi lo sobre escribimos (modificamos)
print(my_dict["Edad"])

my_dict["calle"]= "calle 13" # asi agregamos un dato
print(my_dict)

del my_dict["calle"] # asi eliminamos un elemento
print(my_dict)

print("fabri" in my_dict) # por mas que este "fabri", da false, ya uqe busca por clave, no por valor
print("nombre" in my_dict) # esta es la manera correcta saber si esta o no

print(my_dict.items()) # ITEMS NOS SEPARA UNO POR UNO LOS DICCIONARIOS, (CLAVE, VALOR) , (CLAVE, VALOR), ETC
print(my_dict.keys()) # KEYS NOS RETOMA, LOS KEYS, OSEA, LAS CLAVES (NOMBRE DE CLAVES) EN FORMA DE LISTAS
print(my_dict.values())  # vALUES, AL CONTRARIO DE KEYS, NOS RETORNA LOS VALORES, 

new_dicts= dict.fromkeys(("nombre", 1, "piso")) # CON FROMKEYS, creamos una dicts con clave, pero valor "NONE"}
print(new_dicts) # ENTONCES PODEMOS ASIGNAR NUEVOS VALORES

