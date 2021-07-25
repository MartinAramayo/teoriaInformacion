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

print("Los ultimos bordes pasalos a la base que te interesa")
print("Donde queda la ultima x definimos el codigo [1, 0, 0, 0]")

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
print("Los ultimos bordes pasalos a la base que te interesa")

aux = """
>> v0 = [cero, sp.Rational(3, 4), uno]
>> valor = sp.Rational(9, 16) 
>> arithmetic_value(v0, valor, 5)
"""
print(aux)

v0 = [cero, sp.Rational(3, 4), uno]
valor = sp.Rational(9, 16) 
arithmetic_value(v0, valor, 5)

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