class google_classroom:
  
	"atríbutos"
	 materias=8
	 profesores= 8
   alumnos= 20
	 apartado_comentarios=1

	#métodos

	def calificación(self):
		print("calificación")

	def revisión(self):
		print("revisión")

	def __init__(self):
		pass


class google_classroom(google_clasroom):

	#atríbutos

	color="amarillo y verde"
	apartado_pendientes= 1

	#métodos

	def retardios(self):
		print("retardios")

	def terminadas(self):
		print("terminadas")

	def __init__(self):
		print("constructor de google_classroom")
		pass
print("materias")
str(google_classroom.materias))
print("profesores= " + str(google_classroom.profesores))
print("alumnos= " + str(google_classroom.alumnos))
print("color= " + str(google_classroom.color))
print("apartado_comentarios= " + str(google_classroom.apartado_comentarios))
google_classroom.calificación()
google_classroom.revisión()
google_classroom.retardios()
google_classroom.terminadas()
