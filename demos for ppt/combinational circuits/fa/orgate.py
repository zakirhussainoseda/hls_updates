from myhdl import *

@block
def orgate(a,b,y):

    """
    OR Gate
    y - outputs
    a,b - inputs

    """

    @always_comb
    def comb():
        if a==0 and b==0:
            y.next=0
        elif a==0 and b==1:
            y.next=1
        elif a==1 and b==0:
            y.next=1
        else:
            y.next=1

    return comb

def convert():
    a,b,y = [Signal(bool(0)) for i in range(3)]
    convInst =orgate(a,b,y)
    convInst.convert(hdl='Verilog')

convert()