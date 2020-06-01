class serie_tv:
  "Atríbuto"

  genero= "drama"
  actores= "30"
  horario= "7-8pm"
  canal= "308"
  difinicion = "hd"
  edad= "mayores_13"
  capitulos = "10"
  idioma= "inglés-español"
  duracion= "1hora"
  trama="tristeza"
 
  "Métodos"
  def entretener(self):
    print("entretener")
  def emociones(self):
    print("emociones")
  def aprendizaje(self):
    print("aprendizaje")
  def dinero(self):
    print("dinero")
  def audencia(self):
    print("audencia")  

  def _init_(self):
    print("atributos serie_tv")
    print("genero="+str(self.genero))
    print("actores"+str(self.actores))
    print("horario="+str (self.horario))
    print("canal="+str(self.canal))
    print("definicion"+str(self.difinicion))
    print("edad="+str(self.edad))
    print("capítulos="+str(self.capitulos))
    print("idioma="+str(self.idioma))
    print("duracion="+str(self.duracion))
    print("trama="+str(self.trama))
    
objeto = serie_tv()
objeto.entretener()
objeto.emociones()
objeto.aprendizaje()
objeto.dinero()
objeto.audencia()
objeto._init_()