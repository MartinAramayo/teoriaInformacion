import sympy as sp
from copy import copy

# Aesthetic

def tag_list(size):
    if size >= 2:
        tag = size * ['│']
        tag[0], tag[-2], tag[-1] = '│sup', '│inf', '│code'
        return tag

def str_algo_step(a_list, k):
    a = [f'{k}', f'{a_list[0]}', '┼']
    for index in range(len(a_list)-1):
        a += ['│', '╳', '│'] if k == index else 3 * ['│']
        not_finished = (a_list[-1] != a_list[index+1])
        a += [f'{a_list[index+1]}'] if not_finished else []
    a += ['┼', f'{a_list[-1]}']
    a.reverse()
    return a
        
def steps2stringTable(table):
    ancho = max(len(max(col, key=len)) for col in table)
    num_filas = len(table[0])
    num_columnas = len(table)
    table_str = ''
    for indx_table, fila in enumerate(zip(*table)):
        for indx in range(len(fila)-1):
            table_str += str([*fila][indx]).center(ancho)
            table_str += ' '
        table_str += str([*fila][indx+1])
        table_str += '\n'
        # introduce a double line to separete the answer
        if indx_table == (num_filas-2):
            # all columns, except tag (last one)
            all_steps_width = (num_columnas - 1)*(ancho + 1)
            table_str += '\n' + all_steps_width * '=' + '\n'
    return table_str, ancho, num_filas, num_columnas

# Calculation

def new_value(start, end, frac):
    """Get value at a fraction of an interval

    Args:
        start (number): Start of interval
        end (number): End of interval
        frac (number): Fraction of interval

    Returns:
        number: Value at a fraction of an interval
    """
    return (end - start) * frac + start

def algo_step(v_base, v_now, digit):
    v_next = len(v_base)*[0]
    start, end = v_now[digit], v_now[digit+1]
    v_next[0], v_next[-1] = start, end
    for indx in range(1, len(v_base)-1):
        v_next[indx] = new_value(start, end, v_base[indx])
    return v_next

def arithmetic(v0, code):
    v_here, lista_sol = v0, []
    for digit in code:
        lista_sol.append(str_algo_step(v_here, digit))
        v_here = algo_step(v0, v_here, digit)
    
    tag = tag_list(len(lista_sol[-1]))
    lista_sol.append(tag)
    aux = steps2stringTable(lista_sol)
    table_str, ancho, num_filas, num_columnas = aux
    
    all_steps_width = (num_columnas-1)*(ancho + 1)
    print(all_steps_width * '-')
    print(table_str)
    print(all_steps_width * '-')

def algo_step_value(v_base, v_now, valor):
    for indx in range(len(v_base)-1):
        if v_now[indx] == valor:
            return v_now, indx
        if v_now[indx+1] == valor:
            return v_now, indx + 1 
        in_interval = (v_now[indx] < valor 
                       and valor < v_now[indx+1])
        digit = indx if in_interval else -1
        if digit != -1:
            break
    return algo_step(v_base, v_now, digit), digit

def arithmetic_value(v0, valor, steps):
    v_here, lista_sol = v0, []
    for _ in range(steps):        
        v_k, digit = algo_step_value(v0, v_here, valor)
        lista_sol.append(str_algo_step(v_here, digit))
        if v_here == v_k:
            break
        v_here = v_k
    
    tag = tag_list(len(lista_sol[-1]))
    lista_sol.append(tag)
    aux = steps2stringTable(lista_sol)
    table_str, ancho, num_filas, num_columnas = aux
    
    all_steps_width = (num_columnas-1)*(ancho + 1)
    prefix = ('valor, ' + str(valor))
    print(prefix + (all_steps_width - len(prefix)) * '-')
    print(table_str)
    print(all_steps_width * '-')

cero = sp.Rational(0, 1) 
uno = sp.Rational(1, 1)