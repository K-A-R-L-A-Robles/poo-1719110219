class estudiante:
  "Atríbuto"

  mochila= "1"
  libreta= "8"
  ropa= "5"
  zapatos= "2"
  computadora = "1"
  lapiceros= "5"
  celular= "1"
  dinero= "200"
  libros= "5"
  cargador="1"
 
  "Métodos"
  def aprender(self):
    print("aprender")
  def concentracion(self):
    print("concentracion")
  def alimentacion(self):
    print("alimentarse")
  def gastar(self):
    print("gastar")
  def socializar(self):
    print("socializar")  

  def _init_(self):
    print("atributos estudiante")
    print("mochila="+str(self.mochila))
    print("libreta"+str(self.libreta))
    print("ropa"+str (self.ropa))
    print("zapatos"+str(self.zapatos))
    print("computadora"+str(self.computadora))
    print("lapiceros"+str(self.lapiceros))
    print("celular"+str(self.celular))
    print("dinero"+str(self.dinero))
    print("libros"+str(self.libros))
    print("cargador"+str(self.cargador))
objeto = estudiante()
objeto.aprender()
objeto.concentracion()
objeto.alimentacion()
objeto.gastar()
objeto.socializar()
objeto._init_()