

def rellenarBits(numero:str,bitsDisponibles:int)->str:
    while len(numero)!=bitsDisponibles:
        numero = "0" + numero
    return numero

def decimalABinario(numeroDecimal:int,bitsDisponibles:int)->str:
    numeroBinario = 0
    multiplicador = 1

    while numeroDecimal != 0:
        numeroBinario = numeroBinario + numeroDecimal % 2 * multiplicador
        numeroDecimal //= 2
        multiplicador *= 10
    numeroBinario = str(numeroBinario)
    
    if len(numeroBinario) < bitsDisponibles:
        return rellenarBits(numeroBinario,bitsDisponibles)

    return numeroBinario

def actualizarPosicion(matrix,paresOcupados,dimensiones)->tuple:  
    filas = dimensiones[0]
    columnas = dimensiones[1]

    for f in range(0,filas):
        for c in range(0,columnas):
            posicion : tuple = (f,c)            
            if posicion not in paresOcupados:
                return posicion
    return (-1,-1)

def devolverMatriz(tamañoMatriz):
    if tamañoMatriz == "2x3":
        matrix = [
            [1,0,0],
            [1,0,1]
        ]
        return matrix
    elif tamañoMatriz == "3x4":
        matrix = [
            [0,2,2,2],
            [1,1,1,0],
            [1,0,2,0]
        ]
        return matrix
    elif tamañoMatriz == "4x5":
        matrix = [
            [0,1,0,2,2],
            [3,2,0,1,3],
            [2,3,3,3,2],
            [1,1,1,0,0]
        ]
        return matrix
    elif tamañoMatriz == "5x6":
        matrix = [
            [4,3,2,0,4,3],
            [0,0,1,0,2,2],
            [1,4,0,3,2,2],
            [1,4,1,4,0,1],
            [2,4,1,3,3,3]
        ]
        return matrix
    else:
        return "Opción no válida"
