

def rellenarBits(numero:str,bitsDisponibles:int)->str:  # Medicion analitica: 4n + 1
    while len(numero)!=bitsDisponibles: # 1 + 1 = 2  -> Resultado del ciclo 4n
        numero = "0" + numero # 1 + 1 = 2
    return numero # 1

def decimalABinario(numeroDecimal:int,bitsDisponibles:int)->str: # Medicion analitica: 10n + 9
    numeroBinario = 0 # 1
    multiplicador = 1 # 1

    while numeroDecimal != 0: # 1 + 1 = 2 -> Resultado del ciclo 10n
        numeroBinario = numeroBinario + numeroDecimal % 2 * multiplicador # 1 + 1 + 1 + 1 = 4 
        numeroDecimal //= 2 # 1 + 1 = 2 
        multiplicador *= 10 # 1 + 1 = 2
    numeroBinario = str(numeroBinario) # 1 + 1 = 2
    
    if len(numeroBinario) < bitsDisponibles: # 1 + 1 = 2
        return rellenarBits(numeroBinario,bitsDisponibles) # 1 + 1 = 2

    return numeroBinario # 1

def actualizarPosicion(matrix,paresOcupados,dimensiones)->tuple:  # Medicion analitica: 10n^2 + 5
    filas = dimensiones[0] # 1 + 1 = 2 
    columnas = dimensiones[1] # 1 + 1 = 2

    for f in range(0,filas): # 2 -> Resultado del ciclo 2n*5n = 10n^2
        for c in range(0,columnas): # 2 -> Resultado del ciclo 5n
            posicion : tuple = (f,c) # 1     
            if posicion not in paresOcupados: # 1 
                return posicion # 1
    return (-1,-1) # 1

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
