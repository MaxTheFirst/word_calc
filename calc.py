from math import *
import re
import replacements
import patterns

def tg(x):
    return tan(x)

def ctg(x):
    return 1 / tan(x)

def arcctg(x):
    return pi / 2 - atan(x) 

def all_replace(eq: str):
    for arg in replacements.REPLACEMENTS:
        eq = eq.replace(*arg)
    return eq

def replace_roots(eq: str):
    for key, val in enumerate(replacements.ROOTS):
        parts = re.findall(patterns.ROOT[0].format(val), eq)
        for part in parts:
            arg = re.findall(patterns.ROOT[1].format(val), part)[0]
            eq = eq.replace(part, patterns.ROOT[2].format(key+2, arg), 1)
    return eq

def replace_re(eq: str, pattert, arg_pattern, new):
    parts = re.findall(pattert, eq)
    for part in re.finditer(pattert, eq):
        arg = re.findall(arg_pattern, part.group())[0]
        if '&' in arg:
            arg = arg.split('&')
        elif ' ' in arg:
            arg = arg.split(' ')
        else:
            arg = [arg]
        eq =  eq[:part.start()] + new.format(*arg[::-1]) + eq[part.end():]
    return eq

def replaces_re(eq: str, index = None):
    for pattert, arg_pattern, new in patterns.REP_RE[1::]:
        eq = replace_re(eq, pattert, arg_pattern, new)
    return eq

def get_calc(eq):

    eq = all_replace(eq)
    eq = replace_re(eq, *patterns.REP_RE[0])
    eq = replace_roots(eq)
    eq = replaces_re(eq)
    result = eval(eq)
    return str(result).replace('.', ',')