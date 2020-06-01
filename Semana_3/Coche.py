class coche:
   
  "atríbutos"
  llantas= 4
  acientos=5
  volante= 1
  espejos= 2
  puertas= 4
  
  #métodos

  def encender(self):
    print("encender")

  def acelerar(self):
    print("acelersr")

  
  def __init__(self):
    pass

        

class KIA(coche):
  
  #atríbutos
  
  Capacidad_de_pasajeros= 5
  ventanas""=4

  #métodos

  def  velocidad_maxima(self):
    print("Velocidad máxima:176.28")

  def transportarse(self):
    print("transportarse")

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
KIA.encender()
KIA.acelerar()
KIA.velocidad_maxima()
KIA.transportarse()