from arithmetic import *

print("Codificando la secuencia")
aux = """
>> v0 = [cero, sp.Rational(3, 4), uno]
>> code = [0, 0, 1, 1, 0]
>> arithmetic(v0, code)
"""
print(aux)

v0 = [cero, sp.Rational(3, 4), uno]
code = [0, 0, 1, 1, 0]
arithmetic(v0, code)

print("Los últimos bordes, se pueden pasar a la base de salida")
print("En este caso, en base 2, el supremo e ínfimo:")
print(""" 
> 567/1023 to base 2
      567 / 1023 ≈ 0000,100011011110001101111000110111100
> 135/256 to base 2
      135 / 256 = 0000,10000111
""")
print("Lo que implica que el código final es: [1, 0, 0, 0]")

print("================================================")

aux = """
>> v0 = [cero, sp.Rational(1, 2), uno]
>> code = [1, 0, 0, 0]
>> arithmetic(v0, code)
"""
print(aux)

v0 = [cero, sp.Rational(1, 2), uno]
code = [1, 0, 0, 0]
arithmetic(v0, code)

print("Decodifico el valor que saque de lo anterior")
print("Los últimos bordes pasalos a la base que te interesa")

print("================================================")

aux = """
>> v0 = [cero, sp.Rational(3, 4), uno]
>> valor = sp.Rational(9, 16) 
>> arithmetic_value(v0, valor, 5)
"""
print(aux)

v0 = [cero, sp.Rational(3, 4), uno]
valor = sp.Rational(9, 16) 
arithmetic_value(v0, valor, 5)

print("================================================")

aux = """
>> v0 = [cero, sp.Rational(3, 4), uno]
>> valor = sp.Rational(1, 2) 
>> arithmetic_value(v0, valor, 5)
"""
print(aux)

v0 = [cero, sp.Rational(3, 4), uno]
valor = sp.Rational(1, 2) 
arithmetic_value(v0, valor, 5)

print("Resuelvo y obtengo que [0, 1]") 

print("================================================")

aux = """
>> v0 = [cero, sp.Rational(1, 2), uno]
>> valor = sp.Rational(1, 2) 
>> arithmetic_value(v0, valor, 5)
"""
print(aux)

v0 = [cero, sp.Rational(1, 2), uno]
valor = sp.Rational(1, 2) 
arithmetic_value(v0, valor, 5)

print("Resuelvo y obtengo que [1]") 