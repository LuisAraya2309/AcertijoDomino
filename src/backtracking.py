from funcionesAuxiliares import *

#Algoritmo de backtracking

def backtracking(matrix):
    
    # Instanciamiento de variables
    set = len(matrix) - 1
    filas = set+1
    columnas = filas +1 
    bitsDisponibles = (filas * columnas)//2
    combinaciones = 2**(bitsDisponibles)
    soluciones = []
    
    posiblesSoluciones = []
    #Se llena la lista con las posibles soluciones del algoritmo
    for i in range(0,combinaciones):
        posibleSolucion = decimalABinario(i,bitsDisponibles)
        posiblesSoluciones.append(posibleSolucion)
    #Ciclo principal donde se realiza la poda del backtraking
    iterador = 0 
    while iterador<len(posiblesSoluciones):
        
        posibleSolucion = posiblesSoluciones[iterador]
        fichasUsadas = []
        paresOcupados = []
        solucionProbada =  True
        
        for e in range(0,len(posibleSolucion)): 
            
            solucionDescartada = ""
            posicionActual : tuple = actualizarPosicion(matrix,paresOcupados,(filas,columnas))

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
                solucionProbada = False
                solucionDescartada = posibleSolucion[:e+1]
                break

            if ficha in fichasUsadas:
                solucionDescartada = posibleSolucion[:e+1]
                solucionProbada = False
                break
            else:
                fichasUsadas.append(ficha)
                paresOcupados.append(posicionA)
                paresOcupados.append(posicionB)

        if solucionProbada:
            soluciones.append(posibleSolucion)
            iterador+=1
        else:
            indice = 0
            while indice<len(posiblesSoluciones):
                elemento = posiblesSoluciones[indice]
                if elemento[:len(solucionDescartada)] == solucionDescartada:
                    posiblesSoluciones.remove(elemento)
                else:
                    indice+=1

    return soluciones





