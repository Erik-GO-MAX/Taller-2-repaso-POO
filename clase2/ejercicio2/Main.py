from Estudiante import  Estudiante

def llenar_lista_estudiantes():
    lista_estudiantes = []
    for i in range(8):
        nombre = input(f"ingrese el nombre del estudiante {i + 1}: ")
        sexo = input(f"ingrese el sexo del estudiante {i + 1}: ")
        edad = int(input(f"ingrese la edad del estudiante {i + 1}: "))
        nota = float(input(f"ingrese la nota de el estudiante {i + 1}: "))
        mi_estudiante = Estudiante(nota=nota, edad=edad, sexo=sexo, nombre=nombre)
        lista_estudiantes.append(mi_estudiante)
    return lista_estudiantes

def seleccionar_estudiantes(lista_estudiantes, lista_estudiante_aprobados):
    for estudiante in lista_estudiantes:
        if (estudiante.getNota() >= 4.5):
            lista_estudiante_aprobados.append(estudiante)
    return lista_estudiante_aprobados

def contar_estudiantes_aprobados(lista_estudiantes_aprobados):
    hombres_aprobados = 0
    mujeres_aprobadas = 0
    for estudiante in lista_estudiantes_aprobados:
        if(estudiante.getSexo() == "hombre"):
            hombres_aprobados += 1
        else:
            mujeres_aprobadas += 1
    print(f"el numero de mujeres que aprobo la asignatura de programacion con una nota mayor o igual a 4.5 es: {mujeres_aprobadas}")



    

class Main():
    def main():
        lists_aprobados = []


        lista_estudiante1 = llenar_lista_estudiantes()
        lista_estudiante2 = llenar_lista_estudiantes()

        lista_aprobados = seleccionar_estudiantes(lista_estudiante1, lista_aprobados)
        lista_aprobados = seleccionar_estudiantes(lista_estudiante2, lista_aprobados)

        contar_lista_aprobados(lista_aprobados)

        for estudiante in lista_aprobados:
            print("El(La) estudiante"+estudiante.getNombre()+"aprobo la agsinatura de programacion")
        
        main()