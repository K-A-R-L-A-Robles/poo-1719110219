
class palindromo1: #Es para definir mi clase  
    def _init_(self):#definí mi constructor
        pass
    def palindromo(self): #formas derealizar comparaciones entre cadenas
        respuesta = "S" # es una respuesta que indica que estas en lo correcto o estas de acuerdo
        
        while respuesta == "S" or respuesta== "s": # mientras sea verdad iterara todo
            cad = input("inserta tu cadena de texto: \n") # Insertamos la cadena a analizar
            numeroespacios= 0 # Almacenara el numero de espacios iniciando mi contador en cero
            cad = cad.lower() # Reemplaza las mayusculas por minusculas
            for espacios in cad: # Analizara la cadena
                if espacios in " ": #Cada espacio será contado
                    numeroespacios +=1
            print("Numero de espacios: " +str(numeroespacios)) 
            cad = cad.lower().replace(" ","").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")# Convierte todas las mayusculas en minusculas,quita espacios, remplaza letras mayusculas por minusculas
            numerovocales = 0 # Almacena el numero de vocales que encuentre una cadena de texto
            for vocales in cad: # Analiza  los valores de la cadena de texto
                if vocales in ("áéíóúaeiou"):
                    numerovocales += 1 # Cada vocal se contará
            print("Numero de vocales: ",numerovocales)
            palindromo = "" #esta variable almacenara la cadena de texto invertida
            for a in cad: #la variable a tendra como inicio de la cadena de texto
                palindromo = a + str(palindromo) # se invertira la pocision de la cadena
            if cad == palindromo: # el if analizara la cadena de texto
                print("El texto es un Palindromo") # si el texto es un palindromo imprimira su veracidad
            else:    
                print("La cadena No es un palindromo") #si no esun palindromo imprimira que no es un palindromo
            respuesta= input("Desea anlizar otra cadena? s/n: ") #pregunte si el usuario desea ingresar otra cadena de texto para iterarla
            if respuesta == "n" or respuesta == "N": 
                break #Fin del analisis

textopalindromo = palindromo1()
textopalindromo.palindromo()