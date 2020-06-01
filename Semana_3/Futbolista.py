class futbolista:
   
  "atríbutos"
  estatura= 1.80
  peso= 70 kg
  uniforme=10
  tenis= 2
  cancha=1
  
  #métodos

  def jugar(self):
    print("jugar")

  def viajar(self):
    print("viajar")

  
  def __init__(self):
    pass

        

class toros(futbolista):
  
  #atríbutos
  
  autobús=1
  equipo=1

  #métodos

  def  condicion_física(self):
    print("condicion_física")

  def equipo(self):
    print("transportarse")

  def __init__(self):
    print("constructor de un avíon Boeing 747")
    pass

toros = toros()

print("alas= "+str(toros.alas))
print("acientos= "+str(toros.acientos))
print("pilotos= "+str(toros.pilotos))
print("libretas= "+str(toros.volantes))
print("ventanillas= "+str(toros.ventanillas))
print("Capacidad de pasajeros= "+str(toros.Capacidad_de_pasajeros))
print("longitud= "+str(toros.longitud))
toros.encender()
toros.apagar()
toros.velocidad_maxima()
toros.transportarse()