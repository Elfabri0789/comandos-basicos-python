# String #

mi_String= "mi string"
mi_otro_string= "aqui hay otro sting"
print(mi_String + " " + mi_otro_string)

mi_saltolinea_string= "este es un\nsalto de linea"
print(mi_saltolinea_string)

mi_tabulacion_string= "\t aca genera un espacio como si usara tab"
print(mi_tabulacion_string)

#formateo

name, surname, age= "fabricio", "ary", 35

print("mi nombre es {} {}  y mi edad es  {} ".format(name, surname, age) ) # manera de formatear datos de variable
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # aca formateamos de forma precisa. %s para string %d para int
print(f"mi nombre es  {name} {surname} y mi edad es {age} ") # colocando la F adelante, podemos hacer un formato mas simple

#desempaquetado de caracteres
lenguaje= "python"
a,b,c,d,e,f= lenguaje  # basicamente lo que hace es pasasle una cantidad de caracteres e indicar cual caracter mostrar en consola
print(d)
print(f)

#division:

lenguaje_slice= lenguaje [1:3] #aca le indicamos que dentro de la variable, nos muestre la letra desde la 1 a la 3
print(lenguaje_slice)

lenguaje_slice= lenguaje [1:] # aca le decimos que nos muestre desde la 1, hasta el final
print(lenguaje_slice)

lenguaje_slice= lenguaje [-2] # aca nos va a mostrar, dos antes que la ultima letra
print(lenguaje_slice)

#reverse

reversed_lenguaje= lenguaje[::-1]
print(reversed_lenguaje) #nos imprime la palabra al reves. 

#metodos o funciones:

print(lenguaje.capitalize()) # capitalize : nos pasa la primera letra a mayuscula
print(lenguaje.upper()) # Upper: nos transforma todo en mayuscula
print(lenguaje.count("t")) # Count: nos cuenta cuantas letras hay, del caracter que le pongamos entre ()
print(lenguaje.isnumeric()) # Isnumeric: nos devuelve un bouleano, diciendo si es o no numerico
print("1".isnumeric()) #Isnumeric: nos devuelve un bouleano, diciendo si es o no numerico
print(lenguaje.lower()) # lower, nos pasa todo a miniscula
print(lenguaje.startswith("py")) # starswith, nos devulve un bouleano, si preguntamos si empieza con tal letra la variable

