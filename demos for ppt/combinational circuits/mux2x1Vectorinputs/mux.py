from myhdl import *

@block
def mux2x1_vectored(y, a, b, sel):

    """ 
    Multiplexer 2x1
    y -- mux output
    a, b -- data inputs
    sel -- control input: select b if asserted, otherwise a

    """

    @always_comb
    def comb():
        if sel == 1:
            y.next = b
        else:
            y.next = a

    return comb

def convert():
    sel = Signal(bool(0))
    a,b,y= [Signal(intbv(0)[8:]) for i in range(3)]
    convInst = mux2x1_vectored(y, a, b, sel)
    convInst.convert(hdl='Verilog')

convert()
