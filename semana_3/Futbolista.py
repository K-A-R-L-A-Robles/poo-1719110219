class futbolista:
   
  "atríbutos"
  estatura= 1.80
  peso= 70 
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
  
  autobus=1
  equipo=1

  #métodos

  def  condicion_fisica(self):
    print("condicion_física")

  def tiempo(self):
    print("tiempo")

  def __init__(self):
    print("constructor de futbolista toros")
    pass

toros = toros()

print("estatura= "+str(toros.estatura))
print("peso= "+str(toros.peso))
print("uniforme= "+str(toros.uniforme))
print("tenis= "+str(toros.tenis))
print("cancha= "+str(toros.cancha))
print("autobus= "+str(toros.autobus))
print("equipo= "+str(toros.equipo))
toros.jugar()
toros.viajar()
toros.condicion_fisica()
toros.tiempo()