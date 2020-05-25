class avion_viajes:
  "Atríbuto"

  alas= "2"
  asientos= "60"
  azafatas= "6"
  pantallas_touch= "60"
  piloto = "2"
  pasajeros= "60"
  baños= "2"
  ventanillas= "30"
  cocina= "1"
  volante="2"
 
  "Métodos"
  def volar(self):
    print("volar")
  def despejar(self):
    print("despejar")
  def encender(self):
    print("encender")
  def apagar(self):
    print("apagar")
  def decender(self):
    print("decender")  

  def _init_(self):
    print("atributos avion_viajes")
    print("alas="+str(self.alas))
    print("asientos"+str(self.asientos))
    print("azafatas="+str (self.azafatas))
    print("pantalla_touch="+str(self.sillas))
    print("computadoras"+str(self.computadora))
    print("pantallas="+str(self.pantallas))
    print("maquina contar billetes="+str(self.maquina_contar_billetes))
    print("copiadora="+str(self.copiadora))
    print("maquina_de_turnos="+str(self.maquina_de_turnos))
    print("altavoces="+str(self.altavoces))
    
objeto = BBVA()
objeto.retirar()
objeto.depositar()
objeto.transferencia()
objeto.ahorro()
objeto.pagar()
objeto._init_()