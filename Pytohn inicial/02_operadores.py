
# operaciones Aritmeticas

print(4 + 2)
print(4  - 2)
print(4 * 2 - 2 + 4 * 3 / 2)
print(4 / 2)
print (4 * 4) 
print(7 %  2) # modulo, es para saber cual es el resto (lo wur sobra), de una division
print(7 // 2) # las 2 //, se llama flor division y lo que hace, es una aproximacion al resultado
print(2 ** 3) # calcular un exponente, una potencia 2x2x2

print("hola " + "python " +  "que tal?") # se puede usar el signo + para concatenar, pero no - / etc
print("hola " + str (5)) #concatena una cadena de texto mas un numero, pero convertido en string
print("hola " * 5) # al agregar un string y multiplicando, se multiplica la palabra! por el numero puesto

my_float= 2.5 *2
print("hola " * int(my_float)) #pasandolo a int, nos deja multiplicar la palabra. pero si queda en float, no

#operadores comparativos

print( 3 < 4 )
print( 3 <= 4 )
print( 3 > 4 )
print( 3 >= 4 )
print( 3 == 4 )
print( 3 != 4 )

print("python" > "hola") # no cuenta caracteres, cuenta ordenacion alfabetica
print("python" > "zona") #por mas que tenga mas caracteres, python empieza con p y zona con z
print (len("python") > len( "zona")) # pero si agregamos len, (lenth) si cuenta caracteres y nos dara python como mayor

# operadores logicos
print( 3 < 4  and ("python" > "hola")) #todo true, es true
print( 3 > 4  or ("python" < "hola")) #en orfalse + false, es false
print( 3 < 4  or ("python" < "hola")) # en or  true + false, es true (es difente al mas por menos = menos)
