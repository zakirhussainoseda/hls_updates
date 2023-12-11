from myhdl import *
from ha import ha
from orgate import orgate

@block
def fa(a,b,c,sum,co):

    s1=Signal(bool(0))
    c1=Signal(bool(0))
    c2=Signal(bool(0))

    ha1=ha(a,b,s1,c1)
    ha2=ha(s1,c,sum,c2)
    orgate1=orgate(c1,c2,co)

    return ha1, ha2, orgate1
def convert():
    a,b,c,sum,co = [Signal(bool(0)) for i in range(5)]
    convInst = fa(a,b,c,sum,co)
    convInst.convert(hdl='Verilog')

convert()