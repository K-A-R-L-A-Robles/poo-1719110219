class BBVA:
  "Atríbuto"

  cajeros= "8"
  escritorios= "10"
  gerente= "1"
  asientos= "30"
  tabletas= "5"
  camaras= "10"
  maquina_contar_billetes = "3"
  copiadoras= "15"
  scaner_de_huella= "20"
  caja_fuerte="1"
 
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
    print("escritorios"+str(self.escritorios))
    print("gerente"+str (self.gerente))
    print("asientos"+str(self.asientos))
    print("tabletas"+str(self.tabletas))
    print("camaras"+str(self.camaras))
    print("maquina_contar_billetes"+str(self.maquina_contar_billetes))
    print("copiadoras="+str(self.copiadoras))
    print("scaner_de_huella"+str(self.scaner_de_huella))
    print("caja_fuerte"+str(self.caja_fuerte))
    
objeto = BBVA()
objeto.retirar()
objeto.depositar()
objeto.transferencia()
objeto.ahorro()
objeto.pagar()
objeto._init_()