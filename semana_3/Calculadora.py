class calculadora:
   
  "atríbutos"
  signos=30
  botones =30
  baterias= 2
  led=1
  carcasa=1
  
  #métodos

  def encender(self):
    print("encender")

  def apagar(self):
    print("apagar")

  
  def __init__(self):
    pass

        

class casio(calculadora):
  
  #atríbutos
  
  color="gris"
  longitud= "15cm"

  #métodos

  def  sumar(self):
    print("sumar")

  def restar(self):
    print("restar")

  def __init__(self):
    print("constructor de casio")
    pass
casio= casio()

print("signos= "+str(casio.signos))
print("botones= "+str(casio.botones))
print("baterias= "+str(casio.baterias))
print("led= "+str(casio.led))
("carcasa= "+str(casio.carcasa))
print("color= "+str(casio.color))
print("longitud= "+str(casio.longitud))
casio.encender()
casio.apagar()
casio.sumar()
casio.restar()