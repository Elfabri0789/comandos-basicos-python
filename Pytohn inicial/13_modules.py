                 ## Modules ##
                # MODULES SIRVE PARA IMPORTAR FICHEROS Y ASI ACCEDER A SUS FUNCIONES.


# FORMA 1 DE IMPORTAR !!!!!

import modulo  # importamos el fichero llamado modulo.

modulo.sumValue (1, 4, 5) # le asignamos los valores. y se imprime en consola
modulo.value ("hola Python") # le asignamos los valores. y se imprime en consola

#FORMA 2 DE HACERLO, ESTO LO PODEMOS HACER IMPORTANDO UN VALOR DE FICHERO, DOS O TODOS

from modulo import sumValue, value # FROM EL NOMBRE DEL FICHERO IMPOR Y LO QUE QUEREMOS IMPORTAR

sumValue (10,34,14)
value("hola pepito")

