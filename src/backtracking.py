from funcionesAuxiliares import *
'''
#1
matrix = [
    [1,0,0],
    [1,0,1]
]
#2
matrix = [
    [0,2,2,2],
    [1,1,1,0],
    [1,0,2,0]
]

#3
matrix = [
    [0,1,0,2,2],
    [3,2,0,1,3],
    [2,3,3,3,2],
    [1,1,1,0,0]
]

#4
matrix = [
    [4,3,2,0,4,3],
    [0,0,1,0,2,2],
    [1,4,0,3,2,2],
    [1,4,1,4,0,1],
    [2,4,1,3,3,3]
]


#Plantilla
matrix = [
    [],
    [],
    [],
    []
]
'''

#Algoritmo principal
def backtracking(matrix)->list:
    set = len(matrix) - 1
    filas = set+1
    columnas = filas +1 
    bitsDisponibles = (filas * columnas)//2
    combinaciones = 2**(bitsDisponibles)
    soluciones = []
    posiblesSoluciones = []
    
    for i in range(0,combinaciones):
        posibleSolucion = decimalABinario(i,bitsDisponibles)
        posiblesSoluciones.append(posibleSolucion)
    
    print(posiblesSoluciones)
    idx = 0
    while idx<len(posiblesSoluciones):
        posibleSolucion = posiblesSoluciones[idx]
        fichasUsadas = []
        paresOcupados = []
        solucionado =  True

        for e in range(0,len(posibleSolucion)): 
            substring = ""
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
                solucionado = False
                substring = posibleSolucion[:e+1]
                break

            if ficha in fichasUsadas:
                substring = posibleSolucion[:e+1]
                solucionado = False
                break
            else:
                fichasUsadas.append(ficha)
                paresOcupados.append(posicionA)
                paresOcupados.append(posicionB)

        if solucionado:
            soluciones.append(posibleSolucion)
            idx+=1
        else:
            index = 0
            while index<len(posiblesSoluciones):
                elemento = posiblesSoluciones[index]
                if elemento[:len(substring)] == substring:
                    posiblesSoluciones.remove(elemento)
                else:
                    index+=1

    return soluciones






def main()->None:
    matrix = [
        [0,2,2,2],
        [1,1,1,0],
        [1,0,2,0]
    ]
    soluciones = backtracking(matrix)
    print('Soluciones: \n')
    print(soluciones)

    
    

main()





