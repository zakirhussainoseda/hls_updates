from myhdl import *

@block
def ha(a,b,sum,co):

    """
    Half Adder
    sum,co - outputs
    a,b - inputs

    """

    @always_comb
    def comb():
        if a==0 and b==0:
            sum.next=0
            co.next=0
        elif a==0 and b==1:
            sum.next=1
            co.next=0
        elif a==1 and b==0:
            sum.next=1
            co.next=0
        else:
            sum.next=0
            co.next=1

    return comb

def convert():
    a,b,sum,co = [Signal(bool(0)) for i in range(4)]
    convInst = ha(a,b,sum,co)
    convInst.convert(hdl='Verilog')

convert()