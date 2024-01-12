# Calculadora de recargas

## Programa base

Las recargas se efectúan mediante una variedad de montos, lo cual puede complicar los cálculos asociados. El programa en consideración tiene la responsabilidad de identificar un monto que cumpla con los requisitos del usuario y proporcionar la correspondiente respuesta. 

Dado un valor específico y un conjunto de montos disponibles, el programa buscará una combinación de elementos de la lista en la que su suma coincida con el valor de entrada. En caso de no encontrar una combinación exacta, elegirá el monto más cercano por exceso y por defecto. Además, se registrarán los valores específicos que contribuyeron a la generación de dichos montos.


Valor exacto:

```
input: 100
lista de montos: [50, 75, 100, 125, 150]
output: [100, 100, [100], [100]]
```

```
input: 80
lista de montos: [20, 30, 40, 50, 60, 70, 80, 90]
output: [80, 80, [80], [80]]
```

Combinacion exacta:
```
input: 110
lista de montos: [20, 30, 40, 50, 60, 70, 80, 90]
output: [110, 110 ,[90, 20], [90, 20]]
```

```
input: 25
lista de montos: [5, 10, 15, 20]
output: [25, 25, [5, 20], [5, 20]]
```

Limites diferentes: 

```
input: 120
lista de montos: [50, 75, 100, 125, 150]
output: [100, 125, [100], [50, 75]]
```

```
input: 180
lista de montos: [50, 75, 100, 125, 150]
output: [175, 200, [75, 100], [150, 50]]
```


---