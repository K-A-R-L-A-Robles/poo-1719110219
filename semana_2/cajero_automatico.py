class BBVA:
  "Atríbuto"

  cajeros= "8"
  ventanillas= "10"
  personal= "50"
  sillas= "30"
  computadora = "25"
  pantallas= "5"
  maquina_contar_billetes = "3"
  copiadora= "15"
  maquina_de_turnos= "1"
  altavoces="4"
 
  "Métodos"
  def retirar(self):
    print("retirar dinero")
  def depositar(self):
    print("depositar")
  def transferencia(self):
    print("transferir dinero")
  def ahorro(self):
    print("ahorrar dinero")
  def pagar(self):
    print("pagar servicios")  

  def _init_(self):
    print("atributos banco BBVA")
    print("cajeros="+str(self.cajeros))
    print("ventanillas"+str(self.ventanillas))
    print("personal="+str (self.personal))
    print("sillas="+str(self.sillas))
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