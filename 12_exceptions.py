 ## EXCEPCIONES ##  MANEJO DE ERRORES##

number_one= 2
number_two= 5
number_two= "5"

# TRY EXCEPT: SI LA EJECUCION ES CORRECTA, SE EJECUTA EL TRY, SI NO, SE EJECUTA EL EXCEPT, PERO EL PROGRAMA CONTINUA
try:
    print(number_one + number_two)
    print( "no a ocurrido ningun error")
except:
    print("se ha producido un error")


# TRY EXCEPT Y ELSE: EL ELSE , SE  EJECUTA, SOLO SI EL TRY ES CORRECTO, SI EL TRY ES INCORRECTO Y LA EJECUCION,
# PASA POR EL EXCEPT, EL ELSE, NO SE EJECUTA

number_three= 2
number_four= 5

try:
    print(number_three + number_four)
    print( "no ah ocurrido ningun error")
except:
    print("se ha producido un error")
else:
    print(" la ejecucion continua correctamente")


## TRY, EXCEPT, ELSE Y FINALLY: EL ELSE , SE  EJECUTA, SOLO SI EL TRY ES CORRECTO, SI EL TRY ES INCORRECTO Y LA EJECUCION,
# PASA POR EL EXCEPT, EL ELSE, NO SE EJECUTA. EL FINALLY, SE EJECUTA SIEMPRE !!

try:
    print(number_three + number_four)
    print( "no ah ocurrido ningun error")
except:
    print("se ha producido un error")
else: # OPCIONAL !!
    print(" la ejecucion continua correctamente")
finally: # OPCIONAL !!
    # SE EJECUTA, SIEMPRE !!!! 
    print("la ejecucion continua")

   
 # TAMBIEN PODEMOS EJECUTAR UN TIPO DE ERROR EN CONCRETO, COMO TYPE ERROR, VALUE ELLOR, ETC, DENTRO DEL EXCEPT
try:
    print(number_one + number_two)
    print( "no a ocurrido ningun error")
except TypeError: # CAMTURAMOS ERRORES TYPE ERROR
    print("se ha producido un TypeError")
except ValueError: # CAMTURAMOS ERRORES TYPE ERROR
    print("se ha producido un ValueError")


# CAPTURA DE LA INFORMACION DE LA EXEPCION ## AGREGANFO AS Y EL NOMBRE DE UNA VARIABLE (EJ ERROR, CARLOS, ETC)
try:
    print(number_one + number_two)
    print( "no a ocurrido ningun error")
except ValueError as error:  # error es un nombre que utilizamos, pero podemos ponerle cualquier nombre
    print(error) # capturamos el error

except Exception as errorExcepcion:
    print(errorExcepcion)