"""Formulas para la conversion de unidades de tiempo"""

def s_a_ms(s):
    return s * 1000

def ms_a_s(ms):
    return ms / 1000

def s_a_min(s):
    return s / 60

def min_a_s(min):
    return min * 60

def min_a_h(min):
    return min / 60

def h_a_min(h):
    return h * 60

def h_a_s(h):
    return h * 3600

def s_a_h(s):
    return s / 3600

def dia_a_h(dia):
    return dia * 24

def h_a_dia(h):
    return h / 24

