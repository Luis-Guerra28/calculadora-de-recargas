def calcularRecarga(monto, listaMontos):
    #Asegurmaos que los montos esten ordenados
    listaMontos.sort()

    com = combinaciones(listaMontos, monto)
    print(com)
    return


def combinaciones(elements, target, currentCombination=[], currentPosition=0, valueMin=0, valueMax=1000000, arrayMin=[], arrayMax=[]):
    total = sum(currentCombination)

    if total > valueMax:
        return [valueMin, valueMax, arrayMin, arrayMax]
    
    if (total >= target) and (total <= valueMax):
        
        valueMax = total
        arrayMax = currentCombination
    
    if (total <= target) and (total >= valueMin):
        valueMin = total
        arrayMin = currentCombination

    for i in range(currentPosition, len(elements)):

        result = combinaciones(
            elements,
            target,
            currentCombination + [elements[i]],
            i,
            valueMin,
            valueMax,
            arrayMin,
            arrayMax
        )
        
        valueMin = result[0]
        valueMax = result[1]
        arrayMin = result[2]
        arrayMax = result[3]

    return [valueMin, valueMax, arrayMin, arrayMax]




print(calcularRecarga(100, [50, 75, 100, 125, 150]))