
# SETS . SET NO ADMITE REPETIDOS (DUPLICADOS), PERO !! NO IMPRIME 2 VECES LO MISMO, NO ES ORDENADO

my_set= set()
my_other_set= {} # inicialmente es un diccionario
print(type (my_other_set)) # inicialmente es un diccionario

my_set= {"javaScrip","Html" , "Python"}
my_other_set={"fabri", "fernandez", 35, 1989} # ahora pasa a ser set
print(type(my_other_set))
print(my_other_set)



my_other_set.add("pepito") # se agrega el elemento, pero a diferencia de las listas, se agrega desordenado
print(my_other_set) # la lista es una estructura ordenada, el set, no

my_other_set.add("fabri") # agregamos un segundo elemento "fabri" y no lo imprime 2 veces
print(my_other_set) #set, no admite doble elemento

print("fabri" in my_other_set) # set si admite busqueda dentro del set con un bouleano
print("fabro" in my_other_set)

my_other_set.remove("pepito")
print(my_other_set) # tambien admite remover un elemento 

my_other_set.clear() # el clear para limpear, si lo admite
print(len(my_other_set)) # con len, vemos cuantos elementos hay en el vector
del my_other_set # del (a diferencia del clear que limpia el set), del lo elimina de raiz
# print(my_other_set)

my_otro_set= {"fabri", "fernandez", 35, 1989}

my_new_set= my_set.union(my_otro_set)  # con .union() unimos dos set
print(my_new_set)
print(my_new_set.union(my_set)) # aca agregarmos otra vez otro set, pero al ser igual que antes y no duplicarse
print(my_new_set) # nos volvera a mostrar el mismo resultado, ya que NO REPITE!

print(my_new_set.difference(my_set)) # nos resta, los elementos de "my_set"

