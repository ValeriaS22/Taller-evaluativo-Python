# Ejercicio 2: Ordenamiento de Frutas en un Salpicón
# En este ejercicio, se requiere desarrollar un programa en Python que permita registrar y organizar un conjunto de frutas con sus respectivos
# precios dentro de un salpicón.

# Ingreso de frutas:
# El programa debe solicitar al usuario el ingreso de 10 frutas, cada una con su nombre y precio
# Almacenar la información en una lista de diccionarios

# Ordenamiento:
# Una vez ingresadas las 10 frutas, el programa deberá ordenarlas de mayor a menor precio y mostrar la lista en pantalla.
# Deben asegurarse de implementar un algoritmo de ordenamiento adecuado para organizar las frutas correctamente y presentar los resultados de forma clara


nombreVendedor = None

frutas = []

opcion = None
print("*** Ordenamiento de Frutas en un Salpicón ***")
print("********")
print("1. Crear las frutas (10)")
print("2. Ordenarla de mayor a menor precio")
print("3. Salir")

while opcion != 5: 
    opcion = int(input("Digita una opción: "))
    
    if opcion == 1:
        print("Bienvenido, vas a crear 10 frutas: ")
        print("********")
        for i in range(10):
            fruta = {} 
            fruta["id"] = len(frutas) + 1
            fruta["Nombre"] = input(f"Digite el nombre de la fruta {i + 1}: ")
            fruta["Precio"] = int(input(f"Digite el precio de la fruta: "))
                
            frutas.append(fruta)
            print(f"Fruta agregada correctamente")
    
    elif opcion == 2:
        print("Lista de helados ordenada de mayor a menor precio:")   
        def ordenar_frutas(frutas):
            ordenado = False
            while not ordenado:
                ordenado = True  
                for i in range(len(frutas) - 1):  
                    if frutas[i]["Precio"] < frutas[i + 1]["Precio"]: 
                        frutas[i], frutas[i + 1] = frutas[i + 1], frutas[i]  
                        ordenado = False 
    
                # Mostramos la lista ordenada
                print("Lista ordenada de mayor a menor precio:")
                for fruta in frutas:
                    print(f"ID: {fruta['id']}, Nombre: {fruta['Nombre']}, Precio: {fruta['Precio']}")
                    
        ordenar_frutas(frutas) 
    elif opcion == 3:
        print("Saliendo del programa...")
    
    else:
        print("Opción no válida por favor inténtalo de nuevo")
        
        
        

