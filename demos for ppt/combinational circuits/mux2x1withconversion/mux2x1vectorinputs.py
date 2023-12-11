from myhdl import *

@block
def muxvectored(y, a, b, sel):

    """ Multiplexer.

    y -- mux output
    a, b -- data inputs
    sel -- control input: select a if asserted, otherwise b

    """
    @always_comb
    def comb():
        if sel == 0:
            y.next = a
        else:
            y.next = b

    return comb

def convert(width=5):
    y, a, b= [Signal(intbv(0)[width:]) for i in range(3)] #Signal(intbv(0)[16:])
    sel = Signal(bool(0))                                #Signal(bool(0))
    convInst = muxvectored(y, a, b, sel)
    convInst.convert(hdl='Verilog')

convert()