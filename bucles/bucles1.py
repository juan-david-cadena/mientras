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
#ejercicio 5 
notas = []
while True :
    notas.append(input(" ingrese sus notas he ingrese 'salir' para finalizar ").lower())
    if notas[-1] == "2" :
        break
notas.pop(-1)
notasfinal = int(notas)
print(notasfinal)