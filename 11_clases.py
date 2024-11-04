# CLASES##

class EmpatyPerson:
    pass            # el pass va cuando la clase no le pasamos valores

print (EmpatyPerson)


class Person:                           # CREAMOS LA CLASE
    def __init__(self, name, surname):  # INIT ES UN CONTRUCTOR DE CLASE, Y SELF ES OBLIGATORIO
        self. name= name               # LLAMAMOS A SELF Y SUS PARAMETROS, LE DAMOS EL VALOR
        self.surname= surname           # SELF SE REFIERE A LA INSTANCIA DE LA CLASE, ES OBLIGATARIO

persona= Person( "fabricio" , "fernandez")
print(persona.name, persona.surname)
   

 ## AGREGAMOS UNA FUNCION A NUESTRA CLASE PERSONITA - (LA CLSE PUEDE TENER MUCHAS FUNCIONES) 

class Personita:                           
    def __init__(self, name, surname, alias = ("SIN ALIAS")):   # CONTRUCTOR INIT
       self.full_name= f"{name} {surname} ({alias})"     # LA F ES CADENA DE TEXTO !!
    
    def walk (self):            # AGREGAMOS LA FUNCIO, WALK
        print(f"{self.full_name} Esta caminando!")


person= Personita( "fabricio" , "fernandez", )
print(person.full_name)
person.walk()
 
  ## LE CAMBIAMOS EL VALOR A LA FUNCION
my_other_person= Personita( "fabricio" , "fernandez" , "PEPITO")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name= "ahora le cambie el nombre al objeto ( y aca pongo el alias en parentesis)"
print(my_other_person.full_name)

my_other_person.full_name= 666  # aca accedimos al valor y le cambiamos de texto a numeros y los cambio sin drama
print(my_other_person.full_name)

# QUEDA EN CLARO DE QUE PYTHON ES UN TIPADO DEBIL, EN EL CUAL. PODEMOS CAMBIAR EL VALOR  DE UNA CADENA DE TEXTO
# A NUMEROS, DE UN VALOR A OTRO . ETC

#VAMOS MOSTAR UN DATO PRIVADO, EL CUAL NO NOS PERMITE VERLO, NI MODIFICARLO

class Avion:
    def __init__(self, parte1, parte2, parte3, parte4):
        self.parte_avion = f"{parte1} {parte2} {parte3} {parte4}" # PROPIEDAD PUBLICA
        self.parte3 = parte3 
        self.__parte4 = parte4  ## ACA CON EL __ LO PONEMO EN PRIVADO, PARA QUE NO PUEDAN VER ESE DATO

   

avion= Avion ("alas" ,"asiento"," ruedas" , "motor")
print(avion.parte_avion)
print(avion.parte3)
print(avion.__parte4)  ## cuando queremos imprimir el parte4, no nos lo va a mostrar

        