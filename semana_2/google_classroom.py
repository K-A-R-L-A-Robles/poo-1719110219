class google_classroom:
  "Atríbuto"

  pendientes= "tareas no hechas"
  tarea= "trabajos"
  comentario= "depende"
  materias= "8"
  camara = "1"
  calendario= "1"
  profesores= "8"
  retardios= "tardar_en_enviar"
  apartado_vinculos= "espacio_subir"
  archivos="documentos"
 
  "Métodos"
  def enviar_trabajos(self):
    print("enviar_trabajos")
  def recibir_trabajos(self):
    print("recibir_trabajos")
  def calificar(self):
    print("calificar")
  def mensajes(self):
    print("mensajes")
  def notificar(self):
    print("notificar")  

  def _init_(self):
    print("atributos google_classroom")
    print("pendientes="+str(self.pendientes))
    print("tarea"+str(self.tarea))
    print("comentario="+str (self.comentario))
    print("materias="+str(self.materias))
    print("camara"+str(self.camara))
    print("calendario="+str(self.calendario))
    print("profesores="+str(self.profesores))
    print("retardios="+str(self.retardios))
    print("apartado_vinculos="+str(self.apartado_vinculos))
    print("archivos="+str(self.archivos))
    
objeto = google_classroom()
objeto.enviar_trabajos()
objeto.recibir_trabajos()
objeto.calificar()
objeto.mensajes()
objeto.notificar()
objeto._init_()