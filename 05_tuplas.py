# Tuples

# la diferencia principal con respecto a las listas, es que los valores son inmutables.
# esto quiere decir que una vez que le asignamos el valor, no se puede cambiar.

mi_tupla= tuple()
mi_otra_tupla= ()

mi_tupla= ("fabri", "fernandez", 35, 1989)
print(mi_tupla)
print(type(mi_tupla))
print(mi_tupla[3])

print(mi_tupla.index(35)) # nos indica en que posision esta el indice del valor en el parentesis

# mi_tupla[2] = 40 # aca nos tira error, ya que el valor original es de 35, y no se puede cambiar

print(mi_tupla [1:3]) #aca hacemos que nos muestre lo que hay entre el elemento 1 y el 3

mi_tupla= list(mi_tupla) # ahi lo podemos cambiar a list, y ya vamos a poder cambiar los datos
print(type(mi_tupla))

del mi_tupla # elimina mi tuple, no el contenido, la tuple completa