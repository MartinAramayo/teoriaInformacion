# teoriaInformacion

Formulas, codigo y ejercicios resueltos de la materia teoría de la información.

## Script para de codificacion aritmetico.

Codificacion aritmetica como si fuese hecha a mano:

Lo que es:
- Un codificador aritmetico que imprime los pasos como lo haria una persona siguiendo el algoritmo a mano.

Lo que no es:
- Una implementacion que pretende ser eficiente o elegante de codificacion aritmetica.

~~~
Codificando la secuencia

>> v0 = [cero, sp.Rational(3, 4), uno]
>> code = [0, 0, 1, 1, 0]
>> arithmetic(v0, code)

---------------------------------
   1       3/4      9/16     9/16     9/16   │sup
   ┼        ┼        ┼        ┼        ┼     │
   │        │        │        │        │     │
   │        │        ╳        ╳        │     │
   │        │        │        │        │     │
  3/4      9/16    27/64   135/256  567/1024 │
   │        │        │        │        │     │
   ╳        ╳        │        │        ╳     │
   │        │        │        │        │     │
   ┼        ┼        ┼        ┼        ┼     │
   0        0        0      27/64   135/256  │inf
   0        0        1        1        0     │input
---------------------------------
Los ultimos bordes pasalos a la base que te interesa
Donde queda la ultima x definimos el codigo [1, 0, 0, 0]

>> v0 = [cero, sp.Rational(1, 2), uno]
>> code = [1, 0, 0, 0]
>> arithmetic(v0, code)

---------------------------------
  1      1     3/4    5/8   │sup
  ┼      ┼      ┼      ┼    │
  │      │      │      │    │
  ╳      │      │      │    │
  │      │      │      │    │
 1/2    3/4    5/8    9/16  │
  │      │      │      │    │
  │      ╳      ╳      ╳    │
  │      │      │      │    │
  ┼      ┼      ┼      ┼    │
  0     1/2    1/2    1/2   │inf
  1      0      0      0    │input
---------------------------------
Decodifico el valor que saque de lo anterior
Los ultimos bordes pasalos a la base que te interesa

>> v0 = [cero, sp.Rational(3, 4), uno]
>> valor = sp.Rational(9, 16)
>> arithmetic_value(v0, valor, 5)

-------------------------valor,  9/16
  1     3/4   │sup
  ┼      ┼    │
  │      │    │
  │      ╳    │
  │      │    │
 3/4    9/16  │
  │      │    │
  ╳      │    │
  │      │    │
  ┼      ┼    │
  0      0    │inf
  0      1    │input
---------------------------------

>> v0 = [cero, sp.Rational(3, 4), uno]
>> valor = sp.Rational(1, 2)
>> arithmetic_value(v0, valor, 5)

-------------------------valor,  1/2
   1       3/4      9/16     9/16   135/256  │sup
   ┼        ┼        ┼        ┼        ┼     │
   │        │        │        │        │     │
   │        │        ╳        │        │     │
   │        │        │        │        │     │
  3/4      9/16    27/64   135/256  513/1024 │
   │        │        │        │        │     │
   ╳        ╳        │        ╳        ╳     │
   │        │        │        │        │     │
   ┼        ┼        ┼        ┼        ┼     │
   0        0        0      27/64    27/64   │inf
   0        0        1        0        0     │input
---------------------------------
Resuelvo y obtengo que [0, 1]
~~~