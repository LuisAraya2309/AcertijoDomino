from funcionesAuxiliares import *

#Algoritmo de fuerza bruta

def fuerzaBruta(matrix):
    
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
                solucionado = False
                break

            if ficha in fichasUsadas:
                solucionado = False
                break
            else:
                fichasUsadas.append(ficha)
                paresOcupados.append(posicionA)
                paresOcupados.append(posicionB)

        if solucionado:
            soluciones.append(posibleSolucion)
    return soluciones






def main():

    soluciones = fuerzaBruta(devolverMatriz("3x4"))
    print('Soluciones: \n')
    print(soluciones)

    
    

main()





