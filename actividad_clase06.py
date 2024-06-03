# while True:
#  n1=float(input("ingresar un numero: "))
#  n2=float(input("ingrese otro numero: "))
#  suma=n1+n2
#  print(f"la suma de {n1} y {n2} es:{int(suma)}")

#  if suma < 10:
#     print("la suma es menor que 10")   
#  else:
#    break    

# lista_comas=input("ingrese lista de numero separados por la coma ")
# lista=(lista_comas.split())
# print(lista)

# def envio():
#     peso=int(input("ingrese el peso de paquete a enviar en hasta 26 kg: "))
#     destino=str(input("ingrese destino al que desea enviar santa cruz/ chubut/ rio negro: "))
#     if peso <= 26 and peso >= 11 and destino.lower() =="santa cruz":
#          print("el costo de envio es de $400")
#     elif peso <= 25 and peso >= 16 and destino.lower()=="chubut":
#          print("el costo de envio es de $420")
#     elif peso <= 26 and peso >= 19 and destino.lower()=="rio negro":
#          print("el costo de envio es de $510")
#     elif peso <= 10 and peso >= 6 and destino.lower() =="santa cruz":
#          print("el costo de envio es de $300")
#     elif peso >= 5 and destino.lower() =="santa cruz":
#          print("el costo de envio es de $200")
#     elif peso <= 15 and peso >= 11 and destino.lower()=="chubut":
#          print("el costo de envio es de $390")
#     elif peso >= 10 and destino.lower()=="chubut":
#          print("el costo de envio es de $350")
#     elif peso <= 18 and peso >= 13 and destino.lower()=="rio negro":
#          print("el costo de envio es de $480")
#     elif peso >= 12 and destino.lower()=="rio negro":
#          print("el costo de envio es de $400")
#     else:
#          print("estan mal los parametros")  

                 
# contador = 0
# while contador <= 12:
#      print(contador) 
#      contador += 1
#      if contador ==10:
#       print("estamos en el 10") 
#       continue
# def saludar(nombre):
#  print(f"Hola {nombre}")
# saludar("gustavo")



# matriz=[
#  [1,2,3],
#  [1,1,2],
#  [1,1,1]
# ]
# print(matriz[0][2])
# matriz.__add__(1)

# lista=[1,2,3,56,85,2,12,56,3,589,156,125]
# print(max(lista))
# lista_ordenada=sorted(lista)
# print(lista_ordenada)

# lista_ordenada=sorted(lista,reverse=True)
# print(lista_ordenada)
# print(lista)
# nueva_lista = lista.sort()
# print(nueva_lista)

# def viaje():
#     precio_conbustible = int(input("ingrese precio del conbustible:"))
#     km_recorridos = int(input("ingrese cantidad de km recorridos: "))
#     tiempo_del_viaje= float(input("ingrese el tiempo que duro el viaje: "))
#     velocidad_promedio = km_recorridos / tiempo_del_viaje
#     consumo_combustible = km_recorridos / 100 * 10
#     print(f"el consumo de combustible es de en litros es {consumo_combustible}")
#     print(f"la velocidad promedio es de {velocidad_promedio} km/h")
#     consumo_100km=precio_conbustible*100
#     print(f"el consumo por 100 km es de ${consumo_100km}")
#     por_km= consumo_combustible / 100  
#     print(f"el consumo por km es de ${por_km}")
#     por_km_peso =

def busqueda_lineal(lista,odjetivo):
    return odjetivo in lista


# numero=[1,5,3]
# while True:
 
#  objetivo=int(input("ingrese un numero que desea buscar: "))

#  if busqueda_lineal(numero,objetivo):
#     print("si esta")
#  else :
#     print("no esta")
#  uso= str(input(" desea usar de nuevo la busqueda s/n?: ")).lower()
#  if uso == "n":
#   break


def suma(*args):
    total=sum(args)
    print(total)

suma(2,3,4,5,6,7,7)