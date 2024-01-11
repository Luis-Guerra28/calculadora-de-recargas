import math
def calcularRecarga(monto, listaMontos):
    #Asegurmaos que los montos esten ordenados
    listaMontos.sort()

    com = combinaciones(listaMontos, monto)
    print(com)
    return


def combinaciones(elements, target, currentCombination=[], currentPosition=0, valueMin=0, valueMax=1000000):
    total = sum(currentCombination)

    if total > valueMax:
        return [valueMin, valueMax]
    
    if (total >= target) and (total < valueMax):
        valueMax = total
    
    if (total <= target) and (total > valueMin):
        valueMin = total

    for i in range(currentPosition, len(elements)):

        result = combinaciones(elements, target, currentCombination + [elements[i]], i, valueMin, valueMax)
        
        valueMin = result[0]
        valueMax = result[1]
        
    return [valueMin, valueMax]











print(calcularRecarga(100, [50, 75, 100, 125, 150]))