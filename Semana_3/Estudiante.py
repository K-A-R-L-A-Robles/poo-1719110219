class estudiante:
   
  "atríbutos"
  mochila=1
  libreta= 8
  plumones=10
  colores=12
  lapicera=1
  
  #métodos

  def aprender(self):
    print("aprender")

  def estudiar(self):
    print("estudiar")

  
  def __init__(self):
    pass

        

class prepa(estudiante):
  
  #atríbutos
  
  uniforme=2 
  libros=10

  #métodos

  def colegiatura(self):
    print("colegiatura:$1500")

  def demostrar(self):
    print("demostrar")

  def __init__(self):
    print("características de estudiante de prepa")
    pass

prepa=prepa()

print("mochila= "+str(prepa.mochila.ventanillas))
print("libreta= "+str(prepa.libreta))
print("plumones= "+str(prepa.pulmones))
print("colores="+str(prepa.colores))
print("lapicera="+str(prepa.lapicera))
print("uniforme="+str(prepa.uniforme))
print("libros="+str(prepa.libros))

prepa.aprender()
prepa.estudiar()
prepa.colegiatura()
prepa.demostrar()