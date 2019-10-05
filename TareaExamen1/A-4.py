alumno1 = [9, 8, 7, 5, 2, 10]
alumno2 = [5,5,5,5,5]
alumno3 = [0,1,2]
alumno4 = [4,2,4,5,7,8]
alumno5 = [1,1,1,1,]
contador = 0
pivote = 0

for i in range(len(alumno1)):
    sumaAlumno1 =  alumno1[i] + pivote
    pivote = sumaAlumno1
calificaion1 = sumaAlumno1 / len(alumno1)


if calificaion1 >= 6:
  contador = contador+1

pivote = 0

for i in range(len(alumno2)):
    sumaAlumno2 =  alumno2[i] + pivote
    pivote = sumaAlumno2
calificaion2 = sumaAlumno2 / len(alumno2)


if calificaion2 >= 6:
  contador = contador+1

pivote = 0

for i in range(len(alumno3)):
    sumaAlumno3 =  alumno3[i] + pivote
    pivote = sumaAlumno3
calificaion3 = sumaAlumno3 / len(alumno3)


if calificaion3 >= 6:
  contador = contador+1

pivote = 0

for i in range(len(alumno4)):
    sumaAlumno4 =  alumno4[i] + pivote
    pivote = sumaAlumno4
calificaion4 = sumaAlumno4 / len(alumno4)


if calificaion4 >= 6:
  contador = contador+1

pivote = 0
for i in range(len(alumno5)):
    sumaAlumno5 =  alumno5[i] + pivote
    pivote = sumaAlumno5
calificaion5 = sumaAlumno5 / len(alumno5)

if calificaion5 >= 6:
  contador = contador+1


porcentaje = (contador / 5) * 100



print("El porcentaje de alumnos aprovados es: " + str(porcentaje) + "%")