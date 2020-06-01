class futbolista:
  "Atríbuto"

  equipo= "1"
  uniforme= "5"
  altura= "1.80"
  peso= "70"
  condición= "demasiada"
  conocientos= "básicos"
  genero = "mujero/hombre"
  edad= "10-30años"
  piernas_largas= "2"
  manos_grandes="2"
 
  "Métodos"
  def ganar(self):
    print("ganar")
  def ejercicio(self):
    print("ejercicio")
  def dinero(self):
    print("dinero")
  def fans(self):
    print("fans")
  def equipo(self):
    print("equipo")  

  def _init_(self):
    print("atributos futbolista")
    print("equipo="+str(self.equipo))
    print("uniforme"+str(self.uniforme))
    print("altura="+str (self.altura))
    print("peso="+str(self.peso))
    print("condicion"+str(self.condicion))
    print("conocimientl="+str(self.conocimiento))
    print("genero="+str(self.genero))
    print("edad="+str(self.edad))
    print("piernas_largas="+str(self.piernas_largas))
    print("manos_grandes="+str(self.manos_grandes))
    
objeto = futbolista()
objeto.ganar()
objeto.ejercicio()
objeto.dinero()
objeto.fans()
objeto.equipo()
objeto._init_()