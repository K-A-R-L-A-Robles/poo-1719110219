class banco:
   
  "atríbutos"
  cajeros= 10
  ventanillas =10
  camaras= 10
  asientos= 50
  bocinas= 4
  
  #métodos

  def atender(self):
    print("atender")

  def pagar(self):
    print("pagar")

  
  def __init__(self):
    pass

        

class BBVA(banco):
  
  #atríbutos
  
  maquina_turnos="1"
  personal= "40"

  #métodos

  def horario(self):
    print("horario:9-16:00pm")

  def prestamos(self):
    print("prestamos")

  def __init__(self):
    print("servidor de un banco")
    pass

 BBVA= BBVA()

print("cajeros= "+str(BBVA.cajeros))
print("ventanillas= "+str(BBVA.ventanillas))
print("camaras= "+str(BBVA.camaras))
print("asientoss= "+str(BBVA.asientos))
print("bocinas= "+str(BBVA.bocinas))
print("maquina_turnos= "+str(BBVA.maquina_turnos))
print("personal= "+str(BBVA.personal))
BBVA.atender()
BBVA.pagar()
BBVA.horario()
BBVA.prestamos()