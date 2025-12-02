"""Formulas para la conversion de unidades de masa"""

# Sistema Internacional
def kg_a_g(kg):
    return kg * 1000

def hg_a_g(hg):
    return hg * 100

def dag_a_g(dag):
    return dag * 10

def dg_a_g(dg):
    return dg / 10

def cg_a_g(cg):
    return cg / 100

def mg_a_g(mg):
    return mg / 1000

def ton_a_g(ton):
    return ton * 1000000

# Sistema Ingles o imperial
def oz_a_lb(oz):
    return oz / 16

def lb_a_oz(lb):
    return lb * 16

def lb_a_st(lb):
    return lb / 14

def st_a_lb(st):
    return st * 14

def lb_a_short_ton(lb):
    return lb / 2000

def short_ton_a_lb(s_ton):
    return s_ton * 2000

# Conversion entre sistemas
def lb_a_kg(lb):
    return lb * 0.4536

def kg_a_lb(kg):
    return kg / 0.4536

def lb_a_g(lb):
    return lb * 453.59

def g_a_lb(g):
    return g / 453.59

def oz_a_g(oz):
    return oz * 28.3495

def g_a_oz(g):
    return g / 28.3495

def ton_a_short_ton(ton):
    return ton * 1.10231

def short_ton_a_ton(s_ton):
    return s_ton / 1.10231