# #ejercicio1 el programa le solicita dos numeros al usuario para luego si ninguna es igual a 0 vuelva a solicitar
# num1 = int(input("ingresa un numero a sumar "))
# num2 = int(input("ingresa un numero a sumar "))
# while num1 != 0 and num2 != 0 :
#     print (f"la suma de {num1} + {num2} es igual a {num1 + num2}")

#     num1 = int(input("ingresa un numero a sumar "))
#     num2 = int(input("ingresa un numero a sumar "))
# print(f"felicidades por fin ingresas un cero, el resultado de tu suma es {num1 + num2}")

# #ejercicio2  se le solicita al usuario la contraseña y despues se compara con la contraseña correcta
# contraseña = input("ingrese la contraseña")
# while contraseña != "python123" :
#     print("Contraseña incorrecta ")
#     contraseña = input("ingrese la contraseña")
# print("contraseña correcta")

# #ejercicio3 se le solicitan productos en bucle al usuario hasta dectectar la palabra 'fin' para detenerse
# lista_compra = [input("ingrese un producto, escriba 'fin' para finalizar ").lower()]
# while True :
#     if "fin" in lista_compra :
#         break
#     else:
#         lista_compra.append(input("ingrese un producto, escriba 'fin' para finalizar ").lower())
# print (f"sus articulos son {lista_compra}")
# #ejercicio4 se le soliocita al usuariop que ingrese numeros en bucle y atravez de un calculo algebraico se detewrmina si es par o impar y cuando el usuario ingrese '00' se para el bucle y se usa el .pop para eliminar el '00' de la lista y mostrar los resultados
# numeros_parim = []
# par = -1
# im = 0
# while True :
#     if 00 in numeros_parim :
#         break
#     else:
#         numeros_parim.append(int(input("ingresa un numero e ingresa '00' para finalizar")))
#         if ((numeros_parim[-1] // 2) * 2) == numeros_parim[-1]:
#             par += 1
#         else :
#             im += 1
# numeros_parim.pop(-1)
# print (f"sus numeros son {numeros_parim} y son {par} pares y {im} impares")
## Ejercicio 5
#notas_real = []

#while True:
#    nota = input("Ingrese su nota en letras y escriba 'salir' para finalizar: ").lower()

#    if nota == "salir":
#        break
#    elif nota == "uno":
#        notas_real.append(1)
#    elif nota == "dos":
#        notas_real.append(2)
#    elif nota == "tres":
#        notas_real.append(3)
#    elif nota == "cuatro":
#        notas_real.append(4)
#    elif nota == "cinco":
#        notas_real.append(5)
#    else:
#        print("Dato inválido")
#total_Notas = sum(notas_real)
#cantidad = len(notas_real)
#print(f"Su promedio de notas es {total_Notas / cantidad}")
##ejercicio6
#tabla = int(input("ingrese el numero del cual desee la tabla de multiplicar"))
#contar = 0
#while contar < 11 :
#	print (f"{tabla} x {contar} = {tabla * contar} \n")
#	contar += 1
#print("fin de la tabla")
##ejercicio7
#secreto = 16
#while True :
#	numero_secreto = int(input(" ingresa un numero he intenta adivinar el numero correcto "))
#	if numero_secreto == secreto:
#		break
#	elif numero_secreto < secreto :
#		print(" incorrecto, el numero es mayor vuelva a intemtarlo ")
#	elif numero_secreto > secreto :
#		print(" incorrecto, el numero es menor vuelva a intentarlo ")
#print(" contraseña correcta ")
#ejercicio8
#Fruta = ("lulo","papaya","huanavana")
#while True :
#	intentos = input("intenta adivinar una de las frutas, ingresala y veamos tu suerte ").lower()
#	if intentos in Fruta :
#		break
#	else :
#		print("incorrecto, volvamos a intentarlo ")
#print("correcto, tenemos un ganador ")
#ejercicio8 
#traduccion = { "hola" : "hello", "nos vemos" : "see you", "miedo" : "fear", "hambre" : "hunger","caja" : "box" }
#while True :
#	traductor = input("esto es un traductor, ingresa una pala para trafucirla, escribe 'salir' para finalizar ").lower()
#	if traductor == "salir":
#		break 
#	elif traductor in traduccion :
#		print (f"la traduccion de {traductor} es {traduccion[traductor]}")
#	else :
#		print ("la palabra solicitada no se encuentra en nuestra base de datos")
# #ejercicio10
# while True :
# 	operacion = int(input("calculadora simple \n ingresa 1 para sumar \n 2 para restar \n 3 para multiplicar \n 4 para dividir \n 5 para salir \n "))
# 	if operacion == 5 :
# 		break
# 	elif operacion == 1 :
# 		operacion1 = int(input(" ingresa el primer numero "))
# 		operacion2 = int(input(" ingresa el segundo numero "))
# 		print (f"el resultado de {operacion1} + {operacion2} = {operacion1 + operacion2}")
# 	elif operacion == 2 :
# 		operacion1 = int(input(" ingresa el primer numero "))
# 		operacion2 = int(input(" ingresa el segundo numero "))
# 		print (f"el resultado de {operacion1} - {operacion2} = {operacion1 - operacion2}")
# 	elif operacion == 3 :
# 		operacion1 = int(input(" ingresa el primer numero "))
# 		operacion2 = int(input(" ingresa el segundo numero "))
# 		print (f"el resultado de {operacion1} * {operacion2} = {operacion1 * operacion2}")
# 	elif operacion == 4 :
# 		operacion1 = int(input(" ingresa el primer numero "))
# 		operacion2 = int(input(" ingresa el segundo numero "))
# 		print (f"el resultado de {operacion1} / {operacion2} = {operacion1 / operacion2}")
# 	else :
# 		print("dato ingresado es incorrecto")
# #ejercicio 11
# Datos_edad = {
#     "nombres" : [],
#     "edades" : []
# }
# while True :
#     Datos_edad["nombres"].append((input("ingresa tu nombre, si desea salir ingrese 'salir' ")).lower())
#     if "salir" in Datos_edad["nombres"] :
#         break
#     Datos_edad["edades"].append(int(input("ingrese su edad ")))
# borrar = Datos_edad["nombres"].pop(-1)
# print (f"sus nombres son {Datos_edad['nombres']} y sus edades son {Datos_edad["edades"]}")
# #ejercicio 12
# colores = ["rojo","verde","amarillo","azul","naranja"]
# while True :
# 	intentos = input("intenta adivinar el color, ingresalo y veamos tu suerte ").lower()
# 	if intentos in colores :
# 		break
# 	else :
# 		print("incorrecto, volvamos a intentarlo ")
# print("correcto, tenemos un ganador ")
# #ejercicio 13
# potencia = int(input("ingrese el numero del cual desee las potencias "))
# contara = 0
# while contara < 6 :
# 	print (f"{potencia} ^ {contara} = {potencia ** contara} \n")
# 	contara += 1
# print("fin de la tabla de potencias ")
# #ejercicio 14
# cuadrados = []
# contadorb = 0
# while contadorb < 5 :
#     cuadrados.append((int((input("ingresa un numero para saber su cuadrado ")).lower())) ** 2)
#     contadorb += 1
# print (f"sus cuadrados son {cuadrados}")
#ejercicio 15
colegio = {
    
}
while True :
    nombres = (input("ingrese el nombre de su estudiante, ingrese 'salir' para finalizar ").lower())
    if "salir" in nombres :
        break
    colegio[nombres] = float(input("ingrese su nota final "))
print (f"sus estudiantes y sus notas son{colegio} \n")