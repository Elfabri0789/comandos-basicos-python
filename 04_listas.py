# listas 

my_list= list()
my_otra_list= []

my_list= [23, 45, 65, 32, 90, 35, 23]

print(my_list)
print(len(my_list))

my_otra_list=[1.81 , "fabri", "fernandez", 35]
print(my_otra_list)

print(type(my_otra_list)) # saber el tipo de elemento

print(my_list[2]) # aca accedemos al tercer elemento de la lista
print(my_list[-1]) # al usar el menos 1,2, etc. cuenta de atras para adelante

print(my_list.count(23)) # cuenta cuantas veces se repite un valor, sea string, double, int, etc

heigth, name, surname, age= my_otra_list
print(name)  # le pasamos el valor de la variable para que imprima, pero si le ponemos carlos, no cambia en nada

print(my_list + my_otra_list) # nos concatena ambas listas 

my_otra_list.append("agregamos elemento a la lista al final")
print(my_otra_list)

my_otra_list.insert(1,"insertamos en cierta position otro elemento")
print(my_otra_list)

my_otra_list[2] = "alfonso" # suplantamos el elemnto 2, por otro elmento 

my_otra_list.remove(35) #eliminamos el elemento seleccionado
print(my_otra_list)

my_list.pop() # elimina por defecto el ultimo elemento INT!
print(my_list)

print(my_list.pop(2)) # nos muetra el elemnt que va a eliminar, que es el que le pasamos
print(my_list)

mi_elemento_pop= my_list.pop()
print(mi_elemento_pop) # guardamos el elemnto eliminado en otra variable

my_list.clear() # con clear eliminamos la lista completa
print(my_list)

# reasignar valor
my_list= "hola mundo"
print(my_list) # como sabemos se reasigna el valor de la lista, a string
print(type(my_list))

my_nueva_lista= my_otra_list.copy() # copiamos la lista. a una nueva variable
print(my_nueva_lista)

lista= [2, 4, 1, 10, 6, 8]
lista.sort() # sort ordena los numeros de menor a myor
print(lista)