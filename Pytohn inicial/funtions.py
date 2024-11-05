# FUNTIONS
# DEF ES LA PALABRA RESERVADA DE LA FUNCION, EN PYTHON
def my_fuction():
    print("esto es una funcion")

my_fuction ()

def sum_two_values (firts_number, second_number):  ### agregamos los parametros
    print(firts_number + second_number)   ### les pasamos que vamos a hacer con esos parametros

sum_two_values (20 , 15)     ### le pasamos los valores
sum_two_values (12,50)
sum_two_values( 11,11)


 ## pasamos los parametro, en return le decimos que va a retornar, creamos una varible, le pasamos los valores 
 ## (esos valores se guarddan en nuestra variable ) y luego imprimimos 
def sum_two_values_whth_return (firts_number, second_number):  ### agregamos los parametros
    return firts_number + second_number ## lo suma, y lo retorna

my_variable= sum_two_values_whth_return( 2,5) # lo guardamos en la variable, 
print(my_variable) # y luego lo imprimimos

def print_name (name, surname):
    print(f"{name}  {surname}" ) # F, es para indicar, que vamos a hacer algun tipo de formateo en el codigo
    

print_name("fernandez" , "fabricio") # aca le pasamos los valores mal, pero podemos decirle como imprimir cada cosa
print_name(name= "Fabricio" , surname= "Fernandez")

# funcion con valor por defecto

def print_name_with_default (name, apellido, alias= "sin alias"): # aca le decimos que si no le damos un valor por defecto
    print(f"{name} {apellido} {alias}" )


print_name_with_default("fabricio", "fernandez" ) # podemos darle un valor, o dejarlo sin valor y utilizara el valor por defecto

# pasar muchos valores con un solo parametro

def pasar_muchos_valores (*texto): # ponemos el * y podremos pasar muchos valores
    print(texto)

pasar_muchos_valores("hola", "como estas?" , "yo bien y vos", "tambien estoy bien ") # le pasamos los valores que querramos



def pasarlo_en_forma_lista(*lista):
    for text in lista:
        print(text)
pasarlo_en_forma_lista("fabri", "fernadez" , "Alfonso")