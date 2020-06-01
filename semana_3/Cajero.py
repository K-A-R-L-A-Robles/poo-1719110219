class cajero:
   
  "atríbutos"
  camara= 1
  pantalla=1
  color= "gris"
  tamaño=1.25
  botones= 60
  
  #métodos

  def encender(self):
    print("encender")

  def retirar(self):
    print("retirar")

  
  def __init__(self):
    pass

        

class BBVA(cajero):
  
  #atríbutos
  apartado_tarjeta=1
  apartado_ticket=1

  #métodos

  def transferir(self):
    print("transferir")

  def ahorrar(self):
    print("ahorrar")

  def __init__(self):
    print("constructor de cajero")
    pass
BBVA=BBVA()

print("camara= "+str(BBVA.camara))
print("pantalla= "+str(BBVA.pantalla))
print("color= "+str(BBVA.color))
print("tamaño= "+str(BBVA.tamaño))
print("botones= "+str(BBVA.botones))
print("apartado_tarjeta= "+str(BBVA.apartado_tarjeta))
print("apartado_tarjeta= "+str(BBVA.apartado_ticket))
BBVA.encender()
BBVA.retirar()
BBVA.transferir()
BBVA.ahorrar()