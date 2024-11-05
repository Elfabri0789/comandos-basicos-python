#  CONDITIONALS

my_conditionals= False

if my_conditionals:
    print("imprimir esto")

print("imprimir esto otro")

my_condition= 6 * 2

if my_condition == 10:
    print("el resultado es igual a 10 ")

print( "el resultado es 12")

if my_condition >= 10:
    print("el resultado es igual a o mayor a  10 ")

print( "el resultado no es mayor o igual a 10")

if my_condition <= 11:
    print("el resultado es igual a o mayor a  11 ")
else:
    print( "else: el resultado no es mayor o igual a 11")


if my_condition >= 9 and my_condition < 20:
    print("la condicion es mayor o igual que 9 y es menor que 20 ")
else:
    print( "else: la condicion, no se cumple")

   
   # IMPORTANTE !!! HAY QUE VER QUE ABAJO DENTRO DE LA MISMA LINEA, SIGUE SIENDO DEL IF, 
   # HACIENDO LA TABULACION, SALE DE LA CONDICION 

my_other_condition = 5 * 6

if my_other_condition  >= 9 and my_other_condition  < 22:
    print("la condicion es mayor o igual que 9 y es mayor que 22 ")
elif my_other_condition == 30:
    print("se ejecuta el elif")    
else:
    print( "else: la condicion, no se cumple")

#cuando hacemos if, elif o else. la ejecucion, se corta en donde es correcta. y luego frena

my_string= ""

if my_string:
    print(" el string vacio , lo toma por defecto como false")
elif not my_string:
    print("si le damos un not, quiere decir esta el string entonces esta vacio")

my_stringe= "hola mundo"

if my_stringe == "hola carlos":
    print("esto solo nos dice que esta vacio")
elif my_stringe== "hola mundo":
    print("aca se ejecuta el hola mundo")    
