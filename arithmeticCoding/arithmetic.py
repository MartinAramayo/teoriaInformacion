import sympy as sp
from copy import copy
import sys 

def choose_tag_style(style='ascii'):
    
    try:
        if style == 'lines':
            return '│', '╳', '┼'
        elif style == 'ascii':
            return '|', 'X', '-'
        else:
            raise RuntimeError
    except RuntimeError:
        print(
            "RuntimeError: " +
            "Invalid styles, use 'lines' or 'ascii'"
        )
        sys.exit()
        return 

# create side tag
def tag_list(size, style):
    pipe, _, _ = choose_tag_style(style)        
    if size >= 2:
        tag = size * [pipe]
        tag[0]  = f'{pipe}sup'
        tag[-2] = f'{pipe}inf'
        tag[-1] = f'{pipe}code'
        return tag

def str_algo_step(interval, k, style):
    pipe, cross, end = choose_tag_style(style)
    crossed = [pipe, cross, pipe] # [|, X, |] 
    uncrossed = 3 * [pipe]        # [|,|,|]
    
    output = [f'{k}', f'{interval[0]}', end]
    for index in range(1, len(interval)):
        output += crossed if k == index-1 else uncrossed
        finished = (interval[-1] == interval[index])
        output += [] if finished else [f'{interval[index]}'] 
    output += [end, f'{interval[-1]}']
    output.reverse()
    return output

# Get the string table size
table_width = lambda x, y : (x - 1) * (y + 1)

# if |r| <1 output between p0 and pf
frac_mid_point = lambda p0, pf , r: p0 + (pf - p0) * r 
        
def steps2stringTable(table):
    ancho = max(len(max(col, key=len)) for col in table)
    n_filas = len(table[0])
    n_columnas = len(table)
    
    table_str = ''
    for indx_table, fila in enumerate(zip(*table)):
        
        # append every row to table_str 
        for indx in range(len(fila)-1):
            table_str += str([*fila][indx]).center(ancho)
            table_str += ' '
            
        # add side tag
        table_str += str([*fila][indx+1]) + '\n'
        
        # introduce '=' characters for aesthetics
        if indx_table == (n_filas-2):
            all_steps_width = table_width(n_columnas, ancho)
            table_str += all_steps_width * '=' + '\n'
    return table_str, ancho, n_filas, n_columnas

def algo_step(base_interval, interval, digit):
    new_interval = len(base_interval)*[0]
    start, end = interval[digit], interval[digit+1]
    new_interval[0], new_interval[-1] = start, end
    
    for indx in range(1, len(base_interval)-1):
        new_interval[indx] = frac_mid_point(
            start, end, base_interval[indx]
        )
    return new_interval

def arithmetic(base_interval, code, style='ascii'):
    interval, lista_sol = base_interval, []
    for digit in code:
        str_step = str_algo_step(interval, digit, style)
        lista_sol.append(str_step)
        interval = algo_step(base_interval, interval, digit)
    
    # add right side tag
    tag = tag_list(len(lista_sol[-1]), style)
    lista_sol.append(tag)
    
    # get the width of the table
    aux = steps2stringTable(lista_sol)
    table_str, ancho, num_filas, num_columnas = aux
    all_steps_width = table_width(num_columnas, ancho)
    
    # Print the output table
    table_outline = all_steps_width * '-' 
    print(f'{table_outline}\n{table_str}{table_outline}')

def algo_step_value(base_interval, interval, valor):
    for indx in range(len(base_interval)-1):
        
        if interval[indx] == valor:
            return interval, indx
        elif interval[indx+1] == valor:
            return interval, indx + 1 
        
        in_interval = (interval[indx] < valor 
                       and valor < interval[indx+1])
        if in_interval:
            digit = indx
            break
    return algo_step(base_interval, interval, digit), digit

def arithmetic_value(base_interval, 
                     value, 
                     steps, 
                     style='ascii'):
    interval, lista_sol = base_interval, []
    for _ in range(steps):        
        step_value, digit = algo_step_value(
            base_interval, interval, value
        )
        str_step = str_algo_step(interval, digit, style)
        lista_sol.append(str_step)
        if interval == step_value:
            break
        interval = step_value
    
    # add right side tag
    tag = tag_list(len(lista_sol[-1]), style)
    lista_sol.append(tag)
    
    # get the width of the table
    aux = steps2stringTable(lista_sol)
    table_str, ancho, num_filas, num_columnas = aux
    all_steps_width = table_width(num_columnas, ancho)
    
    # Print the output table
    prefix = ('value=' + str(value))
    print(prefix + (all_steps_width - len(prefix)) * '-')
    print(f"{table_str}{all_steps_width * '-'}")

cero = sp.Rational(0, 1) 
uno = sp.Rational(1, 1)