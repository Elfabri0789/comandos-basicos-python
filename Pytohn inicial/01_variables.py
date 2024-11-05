#Variables

my_variable= "nueva variable string"
print(my_variable)

my_variable_int= 5
print(my_variable_int)

my_variable_bouleana= True
print(my_variable_bouleana)


my_int_transform_string= str(my_variable_int) #con el str adelante de la variable, la convierte en string
print(my_int_transform_string)
print(type(my_int_transform_string))

#concatenacion de variables con la , (coma)
print(my_variable,my_variable_int,my_variable_bouleana) # el print, la transforma todo en cadena de texto

#funciones de sistema
print(len(my_variable)) # .len, es para saber cuantos caracteres hay hasta el final de la variable

#variables en una sola linea: concatenamos y mezclamos string con enteros + cadenas de texto
name, surname, alias, age= "fabricio", "fernandez", "pepo", 35
print("soy", name, surname, "tengo", age, "años", "y me dicen", alias)

"""
# imput, es para preguntas para que el usuario responda, en este caso, en consola:
name= input('cual es tu nombre?') # si cuando pregunta, le cambiamos los valores, la variable, cambia.
age= input('cuantos años tenes?') # siempre se reasignan los valores y toma el ultimo valor
print(name)
print(age)

"""

#ejemplo de que la variable cambia el valor y se reasinga por la ultima linea de codigo:
hola="numero cinco"
hola= 5
print(hola)

