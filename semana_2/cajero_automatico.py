class cajero:
  "Atríbuto"

  crear_cuentas= "muchas"
  botones= "15"
  camara= "1"
  apartado_tarjeta= "1"
  dinero = "mucho"
  pantalla= "1"
  color = "gris"
  apartado_dinero= "1"
  tarjeta_madre= "1"
  conector_de_luz="1"
 
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
    print("atributos cajero")
    print("crear_cuentas="+str(self.crear_cuentas))
    print("botones"+str(self.botones))
    print("camara="+str (self.camara))
    print("apartado_tarjetas="+str(self.apartado_tarjetas))
    print("dinero"+str(self.dinero))
    print("pantalla="+str(self.pantalla))
    print("color="+str(self.color))
    print("apartado_dinero="+str(self.apartado_dinero))
    print("tarjeta_madre="+str(self.tarjeta_madre))
    print("conector_de_luz="+str(self.conector_de_luz))
    
objeto = cajero()
objeto.retirar()
objeto.depositar()
objeto.transferencia()
objeto.ahorro()
objeto.pagar()
objeto._init_()