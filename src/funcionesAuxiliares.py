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