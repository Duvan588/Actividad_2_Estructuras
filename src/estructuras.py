#diccionario por estudiante
estudiantes = {
    "Juan": {
        "curso": "Programación",#memoria estatica inmutable
        "semestre": "2025-2",   
        "calificaciones": [8.5, 9.0, 7.5] #esta lista es la unica modificable dentro de la dupla
    },
    "Ana": {
        "curso": "Zootecnia",
        "semestre": "2025-2",
        "calificaciones": [10, 9.5, 9.0]
    }
}

#mostrar la información de un estudiante
nombre = input("nombre del estudiante: ")
info = estudiantes[nombre]#buscar alumno
print(f"{nombre} - {info['curso']} ({info['semestre']})")
print("Calificaciones:", info["calificaciones"])

#se pedira al usuario si desea modificar o salir
modificar = int(input("desea modificar notas del estudiante? \n ingresar el valor 1 para modificar \n ingresar el valor 2 para salir del programa \n"))

#compararemos la decisión del usuario
if modificar ==1:
    cambio= int(input("agregar:1 , eliminar: 2 o remplazar: 3 \n")) # crearemos las 3 opciones que nos pide el archivo
    if cambio == 1:#por medio de los condicionales procederomos con las acciones deseadas por el usuario
     agregar = float(input("valor a agregar: "))
     estudiantes[nombre]["calificaciones"].append(agregar)#agrega valores a la lista
    elif cambio==2:
       print("Calificaciones:", info["calificaciones"])
       posicion1 = int(input("posicion de la nota: "))
       estudiantes[nombre]["calificaciones"].pop(posicion1)#.pop elimina el valor dependiendo la posicion indicada
       print(estudiantes[nombre]["calificaciones"])
    elif cambio == 3:
       print("Calificaciones:", info["calificaciones"])
       posicion = int(input("posicion de la nota: "))#necesitamos la posicion de la lista (recordar que la primera posicion es la posicion 0)
       cambiar = float(input("valor de la nota: "))
       estudiantes[nombre]["calificaciones"][posicion] = cambiar #se hace el intercambio de notas
       print(estudiantes[nombre]["calificaciones"])
    
    print(f"Promedio: {sum(estudiantes[nombre]['calificaciones']) / len(estudiantes[nombre]['calificaciones']):.2f}")#:.2f redondea a 2 decimales



elif modificar=
r ==2:
   exit()
