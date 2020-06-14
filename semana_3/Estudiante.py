class estudiante:
   
  "atríbutos"
  mochila=1
  libreta= 8
  marca_texto=3
  colores=12
  lapicera=1
  
  #métodos

  def aprender(self):
    print("aprender")

  def estudiar(self):
    print("estudiar")

  
  def __init__(self):
    pass

        

class preparatoria(estudiante):
  
  #atríbutos
  
  uniforme=2 
  libros=10

  #métodos

  def colegiatura(self):
    print("colegiatura:$1500")

  def demostrar(self):
    print("demostrar")

  def __init__(self):
    print("elementos de estudiante de preparatoria")
    pass

preparatoria=preparatoria()

print("mochila= "+str(preparatoria.mochila))
print("libreta= "+str(preparatoria.libreta))
print("marca_texto= "+str(preparatoria.marca_texto))
print("colores="+str(preparatoria.colores))
print("lapicera="+str(preparatoria.lapicera))
print("uniforme="+str(preparatoria.uniforme))
print("libros="+str(preparatoria.libros))

preparatoria.aprender()
preparatoria.estudiar()
preparatoria.colegiatura()
preparatoria.demostrar()