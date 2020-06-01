class coche:
  "Atríbuto"

  llantas= "4"
  ventas= "4"
  volante= "1"
  frenos= "2"
  asientos= "5"
  motor= "1"
  puertas = "4"
  cofre= "1"
  bolsa_de_aire= "1"
  bocinas="2"
 
  "Métodos"
  def encender(self):
    print("encender")
  def apagar(self):
    print("apagar")
  def acelerar(self):
    print("acelerar")
  def frenar(self):
    print("frenar")
  def conducir(self):
    print("conducir")  

  def _init_(self):
    print("atributo coche")
    print("llantas="+str(se.llantas))
    print("ventas"+str(self.ventanas))
    print("volante="+str (self.volante))
    print("frenos="+str(self.frenos))
    print("asientos+str(self.asientos))
    print("motor="+str(self.motor))
    print("puertas="+str(self.puertas))
    print("cofre="+str(self.cofre))
    print("bolsa_de_aire="+str(self.bolsa_de_aire))
    print("bocina="+str(self.bocina))
    
objeto =coche ()
objeto.encender()
objeto.apagar()
objeto.acelerar()
objeto.frenar()
objeto.conducir()
objeto._init_()