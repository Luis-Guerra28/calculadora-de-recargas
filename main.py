def combinaciones(target, elements, currentCombination=[], currentPosition=0, valueMin=0, valueMax=1000000, arrayMin=[], arrayMax=[]):
    elements.sort()
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
            target,
            elements,
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
