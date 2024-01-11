import math
def calcularRecarga(monto, listaMontos):
    #Asegurmaos que los montos esten ordenados
    listaMontos.sort()
    sizeCombination = math.ceil(monto / listaMontos[0]) 
    print(sizeCombination)
    com = combinaciones(listaMontos, sizeCombination)
    print(com)
    return


def combinaciones(elements, sizeCombination, currentCombination=[], currentPosition=0, result=[]): 
    
    if len(currentCombination) == sizeCombination:
        result.append(currentCombination)
        return

    for i in range(currentPosition, len(elements)): 
        combinaciones(elements, sizeCombination, currentCombination + [elements[i]], i)

    return result











print(calcularRecarga(100, [50, 75, 100, 125, 150]))