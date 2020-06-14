
class coche:
   
  "atríbutos"
  llantas= 4
  acientos=5
  volante=1
  espejos=2
  puertas=4
  
  #métodos

  def acelera(self):
    print("acelera")

  def velocidad_maxima(self):
    print("velocidad_maxima")

  
  def __init__(self):
    pass

        

class KIA(coche):
  
  #atríbutos
  
  Capacidad_de_pasajeros= 5
  ventana=4

  #métodos

  def transportarse(self):
    print("transportarse")

  def encender(self):
    print("encender")

  def __init__(self):
    print("constructor de un coche KIA")
    pass 

KIA=KIA()

print("llantas= "+str(KIA.llantas))
print("acientos= "+str(KIA.acientos))
print("volante= "+str(KIA.volante))
print("espejos= "+str(KIA.espejos))
print("puertas= "+str(KIA.puertas))
print("Capacidad de pasajeros= "+str(KIA.Capacidad_de_pasajeros))
print("ventanas= "+str(KIA.ventanas)
KIA.acelera()
KIA.velocidad_maxima()
KIA.transportarse()
KIA.encender()