import sympy as sp
from copy import copy
import sys 

# Aesthetic

lines = {
    'ascii-pipe':  '|',
    'ascii-cross': 'X',
    'ascii-end':   '-',
    'pipe':        '│',
    'cross':       '╳',
    'end':         '┼',
}

def choose_tag_style(style='ascii'):
    
    try:
        if style == 'lines':
            style = ''
        if style == 'ascii':
            style = 'ascii-'
        elif style != 'ascii':
            raise RuntimeError
    except RuntimeError:
        print(
            "RuntimeError: " +
            "Invalid styles, use 'lines' or 'ascii'"
        )
        sys.exit()
    return (lines[style + 'pipe'], 
            lines[style + 'cross'], 
            lines[style + 'end'])

def tag_list(size, style):
    pipe, cross, end = choose_tag_style(style)        
    if size >= 2:
        tag = size * [pipe]
        aux = f'{pipe}sup', f'{pipe}inf', f'{pipe}code'
        tag[0], tag[-2], tag[-1] = aux
        return tag

def str_algo_step(a_list, k, style):
    pipe, cross, end = choose_tag_style(style)
        
    a = [f'{k}', f'{a_list[0]}', end]
    for index in range(len(a_list)-1):
        a += [pipe, cross, pipe] if k == index else 3 * [pipe]
        not_finished = (a_list[-1] != a_list[index+1])
        a += [f'{a_list[index+1]}'] if not_finished else []
    a += [end, f'{a_list[-1]}']
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
            table_str += all_steps_width * '=' + '\n'
    return table_str, ancho, num_filas, num_columnas

# Calculation

def new_value(start, end, frac):
    """Get a value at a fraction of an interval

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

def arithmetic(v0, code, style='ascii'):
    v_here, lista_sol = v0, []
    for digit in code:
        lista_sol.append(str_algo_step(v_here, digit, style))
        v_here = algo_step(v0, v_here, digit)
    
    # add right side tag
    tag = tag_list(len(lista_sol[-1]), style)
    lista_sol.append(tag)
    
    # get the width of the table
    aux = steps2stringTable(lista_sol)
    table_str, ancho, num_filas, num_columnas = aux
    all_steps_width = (num_columnas - 1) * (ancho + 1)
    
    # Print the output table
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

def arithmetic_value(v0, valor, steps, style='ascii'):
    v_here, lista_sol = v0, []
    for _ in range(steps):        
        v_k, digit = algo_step_value(v0, v_here, valor)
        lista_sol.append(str_algo_step(v_here, digit, style))
        if v_here == v_k:
            break
        v_here = v_k
    
    # add right side tag
    tag = tag_list(len(lista_sol[-1]), style)
    lista_sol.append(tag)
    
    # get the width of the table
    aux = steps2stringTable(lista_sol)
    table_str, ancho, num_filas, num_columnas = aux
    all_steps_width = (num_columnas - 1) * (ancho + 1)
    
    # Print the output table
    prefix = ('valor, ' + str(valor))
    print(prefix + (all_steps_width - len(prefix)) * '-')
    print(table_str)
    print(all_steps_width * '-')

cero = sp.Rational(0, 1) 
uno = sp.Rational(1, 1)