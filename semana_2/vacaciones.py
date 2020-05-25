class vacaciones_playa:
  "Atríbuto"

  boletos= "2"
  sandalias= "2"
  maletas= "3"
  hotel= "1"
  habitacion= "1"
  pisina= "3"
  traje_de_baño= "5"
  flotadores= "2"
  dinero= "5000"
  restaurante="2"
 
  "Métodos"
  def relajarse(self):
    print("relajarse")
  def gastar(self):
    print("gastar")
  def conocer(self):
    print("conocer")
  def comprar(self):
    print("comprar")
  def conocer(self):
    print("conocer")  

  def _init_(self):
    print("atributos vacaciones_playa")
    print("boletos="+str(self.boletos))
    print("sandalias="+str(self.sandalias))
    print("maletas="+str (self.maletas))
    print("hotel="+str(self.hotel))
    print("habitacion"+str(self.habitacion))
    print("pisina="+str(self.pisina))
    print("traja_de_baño="+str(self.traje_de_baño))
    print("flotadores="+str(self.flotadores))
    print("dinero="+str(self.dinero))
    print("restaurantes"+str(self.restaurantes))
objeto = vacaciones_playa()
objeto.relajarse()
objeto.gastar()
objeto.conocer()
objeto.comprar()
objeto.conocer()
objeto._init_()