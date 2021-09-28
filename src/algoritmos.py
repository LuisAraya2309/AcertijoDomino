from funcionesAuxiliares import *
import time
from os import remove
import random
#Algoritmos calculadores
def fuerzaBruta(matrix)->str:  #Medicion Analitica:   10n^4 + 43n^2 + 5n + 17
    tiempoInicio = time.time() # 1 + 1  = 2
    set = len(matrix) - 1 # 1 + 1 = 2
    filas = set + 1 # 1 + 1 = 2 
    columnas = filas +1 # 1 + 1 = 2 
    bitsDisponibles = (filas * columnas)//2 # 1 + 1 + 1 = 2 
    combinaciones = 2**(bitsDisponibles) # 1 + 1 = 2
    soluciones = [] # 1
    print(combinaciones)
    for i in range(0,combinaciones): # 2 -> Resultado del ciclo: 10n^4 + 43n^2 + 5n
        posibleSolucion = decimalABinario(i,bitsDisponibles) # 1 + 10n + 9 = 10n + 10
        fichasUsadas = [] # 1
        paresOcupados = [] # 1
        solucionado =  True # 1

        for e in range(0,len(posibleSolucion)): # 1 + 1 + 1 = 3  -> Resultado del ciclo: 10n^3 + 33n 
            #Actualiza la posicion
            posicionActual : tuple = actualizarPosicion(matrix,paresOcupados,(filas,columnas)) # 1 + 10n^2 + 5 = 10n^2 +6
            if posicionActual == (-1,-1): # 1
                solucionado = False # 1
                break

            x = posicionActual[0] # 1 + 1 = 2
            y = posicionActual[1] # 1 + 1 = 2
            
            if posibleSolucion[e] == "0" and y+1<columnas: # 1 + 1 + 1 + 1 + 1 = 5
                ficha:tuple = (matrix[x][y],matrix[x][y+1]) # 1 + 1 + 1 + 1 + 1 + 1 = 6           Se utiliza el primer if para la medición
                posicionA:tuple = (x,y)   # 1                   
                posicionB:tuple = (x,y+1) # 1 + 1  = 2               
            elif posibleSolucion[e] == "1" and x+1<filas: # 1 + 1 + 1 + 1 + 1 = 5
                ficha:tuple = (matrix[x][y],matrix[x+1][y]) # 1 + 1 + 1 + 1 + 1 + 1 = 6     
                posicionA:tuple = (x,y)  # 1                      
                posicionB:tuple = (x+1,y) # 1 + 1  = 2 
            else:
                #Error de rango
                solucionado = False # 1
                break

            if ficha in fichasUsadas: # 1
                #Error de ficha repetida
                solucionado = False #1
                break
            else:
                fichasUsadas.append(ficha) # 1
                paresOcupados.append(posicionA) # 1
                paresOcupados.append(posicionB) # 1

        #Agrega a la lista de soluciones
        if solucionado:
            soluciones.append(posibleSolucion) # 1
    tiempoFinal = time.time() # 2
    return str(tiempoFinal - tiempoInicio) # 1 + 1 = 2


def backtracking(matrix)->str: #Medicion Analitica:  10n^4 + 43n^2 + 29n + 22
    tiempoInicio = time.time() # 1 + 1 = 2
    # Instanciamiento de variables
    set = len(matrix) - 1 # 1 + 1 + 1 = 3
    filas = set+1 # 1 + 1 = 2
    columnas = filas + 1 # 1 + 1 = 2 
    bitsDisponibles = (filas * columnas)//2 # 1 + 1 + 1 = 3 
    combinaciones = 2**(bitsDisponibles) # 1 + 1 = 2 
    soluciones = [] # 1
    
    posiblesSoluciones = [] # 1
    #Se llena la lista con las posibles soluciones del algoritmo
    for i in range(0,combinaciones): # 1 + 1 = 2 -> Resultado del ciclo: 10n^2 + 13n
        posibleSolucion = decimalABinario(i,bitsDisponibles) # 1 + 10n + 9 = 10n + 10
        posiblesSoluciones.append(posibleSolucion) # 1
    #Ciclo principal donde se realiza la poda del backtraking
    iterador = 0 # 1
    while iterador<len(posiblesSoluciones): # 1 + 1 = 2
        
        posibleSolucion = posiblesSoluciones[iterador] # 1 + 1 = 2
        fichasUsadas = [] # 1
        paresOcupados = [] # 1
        solucionProbada =  True # 1
        
        for e in range(0,len(posibleSolucion)): # 1 + 1 + 1 = 3
            
            solucionDescartada = "" # 1
            posicionActual : tuple = actualizarPosicion(matrix,paresOcupados,(filas,columnas)) # 1 + 10n^2 + 5 = 10n^2 +6

            x = posicionActual[0] # 1 + 1 = 2
            y = posicionActual[1] # 1 + 1 = 2

            if posibleSolucion[e] == "0" and y+1<columnas: # 1 + 1 + 1 + 1 + 1 = 5          Se utiliza el primer if para la medición
                ficha:tuple = (matrix[x][y],matrix[x][y+1]) # 1 + 1 + 1 + 1 + 1 + 1 = 6    
                posicionA:tuple = (x,y) # 1              
                posicionB:tuple = (x,y+1) # 1 + 1  = 2   

            elif posibleSolucion[e] == "1" and x+1<filas:  # 1 + 1 + 1 + 1 + 1 = 5
                ficha:tuple = (matrix[x][y],matrix[x+1][y]) # 1 + 1 + 1 + 1 + 1 + 1 = 6       
                posicionA:tuple = (x,y) # 1                             
                posicionB:tuple = (x+1,y) # 1 + 1  = 2   

            else:
                solucionProbada = False # 1 
                solucionDescartada = posibleSolucion[:e+1] # 1 + 1 + 1 = 3   
                break

            if ficha in fichasUsadas: # 1 
                solucionDescartada = posibleSolucion[:e+1] # 1 + 1 + 1 = 3   
                solucionProbada = False # 1 
                break
            else:
                fichasUsadas.append(ficha) # 1 
                paresOcupados.append(posicionA) # 1 
                paresOcupados.append(posicionB) # 1 

        if solucionProbada:
            soluciones.append(posibleSolucion) # 1 
            iterador+=1 # 1 + 1 = 2 
        else:
            indice = 0 # 1
            while indice<len(posiblesSoluciones): # 1 + 1 = 2
                elemento = posiblesSoluciones[indice]  # 1 + 1 = 2
                if elemento[:len(solucionDescartada)] == solucionDescartada:  # 1 + 1 + 1 = 3
                    posiblesSoluciones.remove(elemento) # 1
                else:
                    indice+=1 # 1 + 1
    tiempoFinal = time.time() # 1 + 1 = 2
    return str(tiempoFinal-tiempoInicio) # 1 + 1 + 1 = 3



def fuerzaBrutaG(matrix):
    #Inicio del html
    tiempoFinal = 0.0
    try:
        remove('procesoFuerzaBruta.txt')
        archivo = open('procesoFuerzaBruta.txt','w')
    except:
        archivo = open('procesoFuerzaBruta.txt','w')

    matrizGrafica =""
    for fila in matrix:
        matrizGrafica+="\n" + str(fila)
    docHTML = '''
                  <!DOCTYPE html>

                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        <title>Fuerza Bruta</title>
                        <link rel="stylesheet" href="static/css/stylePlantillaSolucion.css">
                        <link rel="preconnect" href="https://fonts.gstatic.com">
                        <link href="https://fonts.googleapis.com/css2?family=KoHo:wght@200&display=swap" rel="stylesheet">
                    </head>
                    <body>
                        <h1>Solución por Fuerza Bruta</h1>
                        <div class = "proceso">
                            <Form>
                                <h2>Proceso:</h2>
                                <textarea name="proceso" rows="20" cols="30" readonly=»readonly»>
               '''
    inicio = time.time()
    set = len(matrix) - 1
    filas = set+1
    columnas = filas +1 
    bitsDisponibles = (filas * columnas)//2
    combinaciones = 2**(bitsDisponibles)
    soluciones = []
    solucionesGraficas = []

    for i in range(0,combinaciones):
        posibleSolucion = decimalABinario(i,bitsDisponibles)
        proceso:str ="---------------------" "\n" + str(i) + ". Combinación: " + posibleSolucion + ". \nPasos: \n"
        fichasUsadas = []
        paresOcupados = []
        solucionado =  True

        idFicha = 0
        solucionGrafica = matrix
        for e in range(0,len(posibleSolucion)):
            proceso+= ("#" +str(e) + " ")
            #Actualiza la posicion
            posicionActual : tuple = actualizarPosicion(matrix,paresOcupados,(filas,columnas))
            proceso+="Posición: "+str(posicionActual) + "."
            if posicionActual == (-1,-1):
                solucionado = False
                break

            x = posicionActual[0]
            y = posicionActual[1]
            proceso+="Se toma la ficha " 
            if posibleSolucion[e] == "0" and y+1<columnas:
                ficha:tuple = (matrix[x][y],matrix[x][y+1])
                proceso+=str(ficha) + " de manera horizontal. "  
                posicionA:tuple = (x,y)                      
                posicionB:tuple = (x,y+1)                    
            elif posibleSolucion[e] == "1" and x+1<filas:
                ficha:tuple = (matrix[x][y],matrix[x+1][y])
                proceso+=str(ficha) + " de manera vertical. "      
                posicionA:tuple = (x,y)                        
                posicionB:tuple = (x+1,y)     
            else:
                #Error de rango
                solucionado = False
                proceso+="\nError:\nError de rango.\n"  
                break

            if ficha in fichasUsadas:
                #Error de ficha repetida
                solucionado = False
                proceso+="\nError:\n Error de ficha repetida.\n"  
                break
            else:
                fichasUsadas.append(ficha)
                paresOcupados.append(posicionA)
                paresOcupados.append(posicionB)
                solucionGrafica[posicionA[0]][posicionA[1]] = idFicha
                solucionGrafica[posicionB[0]][posicionB[1]] = idFicha
            idFicha+=1
        if i<=99:
            docHTML+=proceso
        else:
            archivo.write(proceso + "\n")
        #Agrega a la lista de soluciones
        if solucionado:
            soluciones.append(posibleSolucion)
            representacion = ""
            for fila in solucionGrafica:
                representacion+="\n" + str(fila)
            solucionesGraficas.append(representacion)
            docHTML+= "#####Solucionado##### \n"
        

    #Cierre del html
    final = time.time()
    docHTML+='''
                </textarea>
                            </Form>
                        </div>

                        <div class = "informacionExtra">
                            <Form >
                                <label for="fduracion">Duración:</label><br>
                                <input type="text" id="fduracion" name="fduracion" readonly=»readonly» value ='''+str(final-inicio)+'''><br>

                                <label for="fintentosRealizados">Intentos realizados:</label><br>
                                <input type="text" id="fintentosRealizados" name="fintentosRealizados" readonly=»readonly» value ='''+str(combinaciones)+''' ><br>
                                
                                <label for="fcantidadSoluciones">Cantidad de soluciones:</label><br>
                                <input type="text" id="fcantidadSoluciones" name="fcantidadSoluciones" readonly=»readonly» value = '''+str(len(soluciones))+''' ><br>
                            </Form>
                            
                        </div>

                        <div class = "resultados">
                            <form action = "/backtracking">
                                <h2>Matriz:</h2>
                                <textarea name="matriz" rows="7" cols="30" readonly=»readonly»>'''+matrizGrafica+'''</textarea>
                                <h2>Ejemplo de solución:</h2>
                                <textarea name="solucion" rows="8" cols="40" readonly=»readonly»> '''+str(solucionesGraficas[random.randint(0,len(solucionesGraficas)-1)])+'''
                                </textarea>
                                <button type="submit">Siguiente</button>
                            </form>
                        </div>

                    </body>
                </html>
             '''
    archivo.close()
    return docHTML

def backtrackingG(matrix):
    #Inicio del html
    tiempoFinal = 0.0
    try:
        remove('procesoBacktracking.txt')
        archivo = open('procesoBacktracking.txt','w')
    except:
        archivo = open('procesoBacktracking.txt','w')
    
    matrizGrafica ="" 

    for fila in matrix:
        matrizGrafica+="\n" + str(fila)
    docHTML = '''
                  <!DOCTYPE html>

                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        <title>Backtracking</title>
                        <link rel="stylesheet" href="static/css/stylePlantillaSolucion.css">
                        <link rel="preconnect" href="https://fonts.gstatic.com">
                        <link href="https://fonts.googleapis.com/css2?family=KoHo:wght@200&display=swap" rel="stylesheet">
                    </head>
                    <body>
                        <h1>Solución por Backtracking</h1>
                        <div class = "proceso">
                            <Form>
                                <h2>Proceso:</h2>
                                <textarea name="proceso" rows="20" cols="30" readonly=»readonly»>
               '''
    # Instanciamiento de variables
    inicio = time.time()
    set = len(matrix) - 1
    filas = set+1
    columnas = filas +1 
    bitsDisponibles = (filas * columnas)//2
    combinaciones = 2**(bitsDisponibles)
    soluciones = []
    solucionesGraficas = []
    posiblesSoluciones = []
    #Se llena la lista con las posibles soluciones del algoritmo
    for i in range(0,combinaciones):
        posibleSolucion = decimalABinario(i,bitsDisponibles)
        posiblesSoluciones.append(posibleSolucion)
    #Ciclo principal donde se realiza la poda del backtraking
    iterador = 0
    intentos = 0 
    while iterador<len(posiblesSoluciones):
        intentos+=1
        posibleSolucion = posiblesSoluciones[iterador]
        proceso:str ="---------------------" "\n" + "Combinación: " + posibleSolucion + ". \nPasos: \n"
        fichasUsadas = []
        paresOcupados = []
        solucionProbada =  True
        idFicha = 0
        solucionGrafica = matrix

        for e in range(0,len(posibleSolucion)): 
            proceso+= ("#" +str(e) + " ")
            solucionDescartada = ""
            posicionActual : tuple = actualizarPosicion(matrix,paresOcupados,(filas,columnas))
            proceso+="Posición: "+str(posicionActual) + "."
            x = posicionActual[0]
            y = posicionActual[1]

            proceso+="Se toma la ficha " 

            if posibleSolucion[e] == "0" and y+1<columnas:
                ficha:tuple = (matrix[x][y],matrix[x][y+1])
                proceso+=str(ficha) + " de manera horizontal. "    
                posicionA:tuple = (x,y)                      
                posicionB:tuple = (x,y+1)

            elif posibleSolucion[e] == "1" and x+1<filas: 
                ficha:tuple = (matrix[x][y],matrix[x+1][y])
                proceso+=str(ficha) + " de manera vertical. "        
                posicionA:tuple = (x,y)                        
                posicionB:tuple = (x+1,y)

            else:
                proceso+="\nError:\nError de rango.\n"  
                solucionProbada = False
                solucionDescartada = posibleSolucion[:e+1]
                break

            if ficha in fichasUsadas:
                solucionDescartada = posibleSolucion[:e+1]
                solucionProbada = False
                proceso+="\nError:\n Error de ficha repetida.\n"  
                break
            else:
                fichasUsadas.append(ficha)
                paresOcupados.append(posicionA)
                paresOcupados.append(posicionB)
                solucionGrafica[posicionA[0]][posicionA[1]] = idFicha
                solucionGrafica[posicionB[0]][posicionB[1]] = idFicha
            idFicha+=1

        if intentos<=50:
            docHTML+=proceso
        else:
            archivo.write(proceso+"\n")

        if solucionProbada:
            soluciones.append(posibleSolucion)
            docHTML+= "#####Solucionado##### \n"
            iterador+=1
            soluciones.append(posibleSolucion)
            representacion = ""
            for fila in solucionGrafica:
                representacion+="\n" + str(fila)
            solucionesGraficas.append(representacion)
            docHTML+= "#####Solucionado##### \n"
        else:
            proceso+="\n Realizando Poda \n Subcadena inválida: "+solucionDescartada + "\n"
            indice = 0
            while indice<len(posiblesSoluciones):
                elemento = posiblesSoluciones[indice]
                if elemento[:len(solucionDescartada)] == solucionDescartada:
                    proceso+="\nCombinación eliminada: "+ elemento+"\n"
                    posiblesSoluciones.remove(elemento)
                else:
                    indice+=1
            docHTML+=proceso
    docHTML+=proceso
    #Cierre del html
    final = time.time()
    docHTML+='''
                </textarea>
                            </Form>
                        </div>

                        <div class = "informacionExtra">
                            <Form >
                                <label for="fduracion">Duración:</label><br>
                                <input type="text" id="fduracion" name="fduracion" readonly=»readonly» value ='''+str(final-inicio)+'''><br>

                                <label for="fintentosRealizados">Intentos realizados:</label><br>
                                <input type="text" id="fintentosRealizados" name="fintentosRealizados" readonly=»readonly» value ='''+str(intentos)+''' ><br>
                                
                                <label for="fcantidadSoluciones">Cantidad de soluciones:</label><br>
                                <input type="text" id="fcantidadSoluciones" name="fcantidadSoluciones" readonly=»readonly» value = '''+str(len(soluciones))+''' ><br>
                            </Form>
                            
                        </div>

                        <div class = "resultados">
                            <form action = "/backtracking">
                                <h2>Matriz:</h2>
                                <textarea name="matriz" rows="7" cols="30" readonly=»readonly»>'''+matrizGrafica+'''</textarea>
                                <h2>Ejemplo de solución:</h2>
                                <textarea name="solucion" rows="8" cols="40" readonly=»readonly»>'''+ str(solucionesGraficas[random.randint(0,len(solucionesGraficas)-1)])+  ''' </textarea>
                            </form>
                        </div>

                    </body>
                </html>
             '''
        
    archivo.close()
    return docHTML