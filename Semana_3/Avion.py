class avion:
   
  "atríbutos"
  alas= 2
  cabina= 1
  azafata=6
  baños= 2
  asientos= 200
  
  #métodos

  def acelerar(self):
    print("acelerar")

  def despegar(self):
    print("despegar")

  
  def __init__(self):
    pass

        

class viva_aerobus(avion):
  
  #atríbutos
 
  ventanillas_disponibles=60.
  color= "blanco"

  #métodos

   def altura_maxima(self):
    print("altura_maxima 41,000 pies")

  def viajar(self):
    print("viajar")

  def __init__(self):
    print("constructor de un avíon viva_aerobus")
    pass

viva_aerobus =viva_aerobus() 

print("alas= "+str(viva_aerobus.alas))
print("cabina= "+str(viva.cabina))
print("azafata= "+str(viva_aerobus.azafata))
print("baños= "+str(viva_aerobus.baños))
print("asientos= "+str(viva_aerobus.asientos))
print("ventanillas_disponibles= "+str(viva_aerobus.ventanillas_disponibles))
print("color= "+str(viva_aerobus.color))
viva_aerobus.acelerar()
viva_aerobus.despegar()
viva_aerobus.altura_maxima()
viva_aerobus.viajar()