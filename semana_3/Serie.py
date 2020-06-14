class serie:
   
  "atríbutos"
  capítulos=10
  canal=235
  género="romance,amor,terror,ficción,"
  duración="1hr"
  
  #métodos

  def entretenimiento(self):
    print("entretenimiento")

  def comercialización(self):
    print("comercialización")

  
  def __init__(self):
    pass

        

class botched (serie):

  #atríbutos
  
  personajes_principales=2
  capitulos_diarios=2

  #métodos

  def horario (self):
    print("horario: 8-9")

  def lecciones(self):
    print("lecciones")

  def __init__(self):
    print("constructor de un avíon Boeing 747")
    pass

 botched=botched ()

print("capítulos = "+str(botched.ccapítulos))
print("canal= "+str(botched.canal))
print("género= "+str(botched.género))
print("duración="+str(botched.duración))

print("personajes_principales personajes_principales = "+str(ao.p))
print("capitulos _diarios= "+str(botched.capitulos_diarios))
botched.entretenimiento()
botched.ccomercialización()
botched.horario()
botched.lecciones() 