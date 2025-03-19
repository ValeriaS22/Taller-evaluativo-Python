#software estructura 
# Se solicita desarrollar un programa en Python que permita la gestión de una lista de helados mediante un CRUD (Crear, Leer, Actualizar y
# Eliminar). Para ello, deberán implementar las siguientes funcionalidades:

# Crear un helado: Solicitar al usuario los datos del helado: nombre, descripción y precio unitario.
# Generar un identificador único y automático para cada helado.
# Almacenar la información en una lista de diccionarios.
# Ver la lista de helados:
# Mostrar en pantalla la lista completa de helados registrados, con su respectivo ID, nombre, descripción y precio.
# Modificar un helado:
# Permitir la modificación de los datos de un helado existente en la lista a partir de su ID.
#Eliminar un helado:
#Permitir al usuario retirar un helado de la lista a partir de su ID.



nombreVendedor = None

helados = []

opcion = None
print("*** Gestión de Helados ***")
print("********")
print("1. Crear un helado")
print("2. Ver la lista de helados")
print("3. Modificar un helado")
print("4. Eliminar un helado")
print("5. Salir")

while opcion != 5: 
    opcion = int(input("Digita una opción: "))
    
    if opcion == 1:
        print("Bienvenido, puedes crear un helado")
        helado = {} 
        helado["id"] = len(helados) + 1
        helado["Nombre"] = input("Digite el nombre del helado: ")
        helado["Precio"] = int(input("Digite el precio del helado: "))
        helado["Descripción"] = input("Digite la descripción: ")
        
        helados.append(helado)
        print("Helado agregado correctamente")
    
    elif opcion == 2:
        print("Lista de helados:")
        for productoSeleccionado in helados:
            print(productoSeleccionado)
            
    elif opcion == 3:
        heladoModificado = int(input("Digita el id del producto que quieres editar: "))
        encontrado = False 

        for heladoBuscado in helados:
            if heladoBuscado["id"] == heladoModificado:
                heladoBuscado["Nombre"] = input("Nuevo nombre: ")
                heladoBuscado["Precio"] = int(input("Nuevo precio: "))
                heladoBuscado["Descripción"] = input("Nueva descripción: ")
                print("Helado modificado con éxito.")
                encontrado = True
                break  

        if not encontrado:
            print("El id no existe")
    
    elif opcion == 4:
        heladoEliminado = int(input("Digita el id del producto que quieres eliminar: "))
        encontrado = False

        for productoBuscado in helados:
            if productoBuscado["id"] == heladoEliminado:
                helados.remove(productoBuscado)
                print("Helado eliminado")
                encontrado = True
                break  

        if not encontrado:
            print("El id no existe")
    
    elif opcion == 5:
        print("Saliendo del programa...")
    
    else:
        print("Opción no válida, por favor inténtalo de nuevo")

