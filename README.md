# teoriaInformacion

Fórmulas, código y ejercicios resueltos de teoría de la información.

~~~
Hoja de formulas:
   formulas/main.pdf
modulo para codificación aritmético:
   arithmeticCoding/arithmetic.py
Script de ejemplo para codificación aritmética:
   arithmeticCoding/ejemplo.py
~~~

## Script para codificación aritmética

Codificación aritmética como si fuese hecha a mano:

Lo que es:
- Un codificador aritmético que imprime los pasos como lo haría una persona siguiendo el algoritmo a mano.

Lo que no es:
- Una implementación que pretende ser eficiente o elegante de codificación aritmética.

A continuación se tiene el resultado de ejecutar ***arithmeticCoding/ejemplo.py***

~~~ python
Codificando la secuencia:

>> interval0 = [0, sp.Rational(3, 4), 1]
>> code = [0, 0, 1, 1, 0]
>> arithmetic(interval0, code)

---------------------------------------------
   1       3/4      9/16     9/16     9/16   |sup
   -        -        -        -        -     |
   |        |        |        |        |     |
   |        |        X        X        |     |
   |        |        |        |        |     |
  3/4      9/16    27/64   135/256  567/1024 |
   |        |        |        |        |     |
   X        X        |        |        X     |
   |        |        |        |        |     |
   -        -        -        -        -     |
   0        0        0      27/64   135/256  |inf
=============================================
   0        0        1        1        0     |code
---------------------------------------------

Pasando los extremos del último intervalo a alguna base, 
se puede determinar el código final a la salida.

En este caso usamos base 2, el supremo e ínfimo:

> 567/1023 to base 2
      567 / 1023 ≈ 0000,100011011110001101111000110111100
> 135/256 to base 2
      135 / 256 = 0000,10000111

Lo que implica que el código final es: [1, 0, 0, 0]

================================================

>> interval0 = [0, sp.Rational(3, 4), 1]
>> valor = sp.Rational(1, 2) 
>> arithmetic_value(interval0, valor, 5)

value=1/2------------------------------------
   1       3/4      9/16     9/16   135/256  |sup
   -        -        -        -        -     |
   |        |        |        |        |     |
   |        |        X        |        |     |
   |        |        |        |        |     |
  3/4      9/16    27/64   135/256  513/1024 |
   |        |        |        |        |     |
   X        X        |        X        X     |
   |        |        |        |        |     |
   -        -        -        -        -     |
   0        0        0      27/64    27/64   |inf
=============================================
   0        0        1        0        0     |code
---------------------------------------------
Con 5 pasos se obtiene [0, 0, 1, 0, 0]
~~~

## Como contribuir

Por su proceso de producción el proyecto cuenta con múltiples errores de ortografía. Correcciones o citaciones a fuentes para verificar las resoluciones también son muy agradecidas.

## Como compilar los documentos

Pre-requisitos:
- pandoc

Los ejercicios resueltos escritos en Markdown (archivos .md). Se compilan mediante

~~~
pandoc -s ejemplo.md -o 'ejemplo.pdf'
~~~

La hoja de fórmulas puede compilarse con pdflatex u otro compilador de archivos LaTeX (.tex)