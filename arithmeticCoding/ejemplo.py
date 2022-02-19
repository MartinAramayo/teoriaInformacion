from arithmetic import *

style = 'lines'

print(
"""Codificando la secuencia:

>> interval0 = [0, sp.Rational(3, 4), 1]
>> code = [0, 0, 1, 1, 0]
>> arithmetic(interval0, code)
"""
)

interval0 = [0, sp.Rational(3, 4), 1]
code = [0, 0, 1, 1, 0]
arithmetic(interval0, code, style=style)

print(
"""
Pasando los extremos del último intervalo a alguna base, 
se puede determinar el código final a la salida.

En este caso usamos base 2, el supremo e ínfimo:

> 567/1023 to base 2
      567 / 1023 ≈ 0000,100011011110001101111000110111100
> 135/256 to base 2
      135 / 256 = 0000,10000111

Lo que implica que el código final es: [1, 0, 0, 0]
"""
)

print("================================================")

aux = """
>> interval0 = [0, sp.Rational(3, 4), 1]
>> valor = sp.Rational(1, 2) 
>> arithmetic_value(interval0, valor, 5)
"""
print(aux)

interval0 = [0, sp.Rational(3, 4), 1]
valor = sp.Rational(1, 2) 
arithmetic_value(interval0, valor, 5, style=style)

print("Con 5 pasos se obtiene [0, 0, 1, 0, 0]") 

# print("================================================")

# print(
# """
# >> interval0 = [0, sp.Rational(1, 2), 1]
# >> code = [1, 0, 0, 0]
# >> arithmetic(interval0, code)
# """
# )

# interval0 = [0, sp.Rational(1, 2), 1]
# code = [1, 0, 0, 0]
# arithmetic(interval0, code, style=style)

# print(
# """
# > 9/16 to base 2
#   9 / 16 = 0000.1001
# > 1/2 to base 2
#   1 / 2 = 0000.1
  
# Lo que implica que el codigo final es [1,0,0]
# """
# )

# print("================================================")

# aux = """
# >> interval0 = [0, sp.Rational(3, 4), 1]
# >> valor = sp.Rational(9, 16) 
# >> arithmetic_value(interval0, valor, 5)
# """
# print(aux)

# interval0 = [0, sp.Rational(3, 4), 1]
# valor = sp.Rational(9, 16) 
# arithmetic_value(interval0, valor, 5, style=style)

# print(
# """
# > 3/4 to base 2
#   3 / 4 = 0000.11
# > 9/16 to base 2
#   9 / 16 = 0000.1001
  
# Lo que implica que el codigo final es [1]
# """
# )

# print("================================================")

# aux = """
# >> interval0 = [0, sp.Rational(1, 2), 1]
# >> valor = sp.Rational(1, 2) 
# >> arithmetic_value(interval0, valor, 5)
# """
# print(aux)

# interval0 = [0, sp.Rational(1, 2), 1]
# valor = sp.Rational(1, 2) 
# arithmetic_value(interval0, valor, 5, style=style)

# print("Resuelvo y obtengo que [1]") 