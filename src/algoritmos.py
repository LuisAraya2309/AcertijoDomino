from funcionesAuxiliares import *
import time
#Algoritmos calculadores
def fuerzaBruta(matrix)->str:
    tiempoInicio = time.time()
    set = len(matrix) - 1
    filas = set+1
    columnas = filas +1 
    bitsDisponibles = (filas * columnas)//2
    combinaciones = 2**(bitsDisponibles)
    soluciones = []

    for i in range(0,combinaciones):
        posibleSolucion = decimalABinario(i,bitsDisponibles)
        fichasUsadas = []
        paresOcupados = []
        solucionado =  True

        for e in range(0,len(posibleSolucion)):
            #Actualiza la posicion
            posicionActual : tuple = actualizarPosicion(matrix,paresOcupados,(filas,columnas))
            if posicionActual == (-1,-1):
                solucionado = False
                break

            x = posicionActual[0]
            y = posicionActual[1]
            
            if posibleSolucion[e] == "0" and y+1<columnas:
                ficha:tuple = (matrix[x][y],matrix[x][y+1])  
                posicionA:tuple = (x,y)                      
                posicionB:tuple = (x,y+1)                    
            elif posibleSolucion[e] == "1" and x+1<filas:
                ficha:tuple = (matrix[x][y],matrix[x+1][y])    
                posicionA:tuple = (x,y)                        
                posicionB:tuple = (x+1,y)     
            else:
                #Error de rango
                solucionado = False
                break

            if ficha in fichasUsadas:
                #Error de ficha repetida
                solucionado = False
                break
            else:
                fichasUsadas.append(ficha)
                paresOcupados.append(posicionA)
                paresOcupados.append(posicionB)

        #Agrega a la lista de soluciones
        if solucionado:
            soluciones.append(posibleSolucion)
    tiempoFinal = time.time()
    return str(tiempoFinal - tiempoInicio)



def fuerzaBrutaG(matrix):
    #Inicio del html
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
    set = len(matrix) - 1
    filas = set+1
    columnas = filas +1 
    bitsDisponibles = (filas * columnas)//2
    combinaciones = 2**(bitsDisponibles)
    soluciones = []

    for i in range(0,combinaciones):
        posibleSolucion = decimalABinario(i,bitsDisponibles)
        proceso:str ="---------------------" "\n" + str(i) + ". Combinación: " + posibleSolucion + ". \nPasos: \n"
        fichasUsadas = []
        paresOcupados = []
        solucionado =  True

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
        docHTML+=proceso
        #Agrega a la lista de soluciones
        if solucionado:
            soluciones.append(posibleSolucion)
            docHTML+= "#####Solucionado##### \n"
        

    #Cierre del html
    docHTML+='''
                </textarea>
                            </Form>
                        </div>

                        <div class = "informacionExtra">
                            <Form >
                                <label for="fduracion">Duración:</label><br>
                                <input type="text" id="fduracion" name="fduracion" readonly=»readonly» value ='''+ fuerzaBruta(matrix) +'''><br>

                                <label for="fintentosRealizados">Intentos realizados:</label><br>
                                <input type="text" id="fintentosRealizados" name="fintentosRealizados" readonly=»readonly» value ='''+str(combinaciones)+''' ><br>
                                
                                <label for="fcantidadSoluciones">Cantidad de soluciones:</label><br>
                                <input type="text" id="fcantidadSoluciones" name="fcantidadSoluciones" readonly=»readonly» value = '''+str(combinaciones)+''' ><br>
                            </Form>
                            <input type="text" id="set" name="set">
                        </div>

                        <div class = "resultados">
                            <Form>
                                <h2>Matriz:</h2>
                                <textarea name="matriz" rows="7" cols="30" readonly=»readonly»>'''+matrizGrafica+'''</textarea>
                                <h2>Ejemplo de solución:</h2>
                                <textarea name="solucion" rows="8" cols="40" readonly=»readonly»> </textarea>
                                <button type="submit">Siguiente</button>
                            </Form>
                        </div>

                    </body>
                </html>
             '''

    return docHTML