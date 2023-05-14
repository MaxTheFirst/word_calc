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

def iter_re(func):
    def wrapper(eq: str, pattern, arg_pattern, *args, **kwargs):
        while True:
            part = re.search(pattern, eq)
            if not part:
                return eq
            arg = re.search(arg_pattern, part.group()).group()
            new_replace = func(arg, *args, **kwargs)
            eq =  eq[:part.start()] + new_replace + eq[part.end():]
    return wrapper

def replace_roots(eq: str):
    for key, val in enumerate(replacements.ROOTS):
        parts = re.findall(patterns.ROOT[0].format(val), eq)
        for part in parts:
            arg = re.findall(patterns.ROOT[1].format(val), part)[0]
            eq = eq.replace(part, patterns.ROOT[2].format(key+2, arg), 1)
    return eq

@iter_re
def replce_root()

@iter_re
def replace_re(new):
    if '&' in arg:
        arg = arg.split('&')
    elif ' ' in arg:
        arg = arg.split(' ')
    else:
        arg = [arg]
    return new.format(*arg[::-1])

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