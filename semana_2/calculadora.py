class caluladora:
  "Atríbuto"

  botones= "30"
  led= "1"
  baterias= "2"
  signos= "20"
  color = "negro"
  tamaño= "mediana"
  grosor = "delgada"
  marca= "barrilito"
  tipo= "científica"
  textura="dura"
 
  "Métodos"
  def cuentas(self):
    print("cuentas")
  def a_pagar(self):
    print("a_apagar")
  def encender(self):
    print("encender")
  def facilitar_trabajo(self):
    print("facilitar_trabajo")
  def calculos(self):
    print("calculos")  

  def _init_(self):
    print("atributos calculadora")
    print("botones="+str(self.botones))
    print("led"+str(self.led))
    print("baterias="+str (self.baterias))
    print("signos="+str(self.signos))
    print("color"+str(self.color))
    print("tamaño="+str(self.tamaño))
    print("grosor="+str(self.grosor))
    print("marca="+str(self.marca))
    print("tipo="+str(self.tipo))
    print("textura="+str(self.textura))
    
objeto = calculadora()
objeto.cuentas()
objeto.a_pagar()
objeto.encender()
objeto.facilitar_trabajo()
objeto.calculos()
objeto._init_()