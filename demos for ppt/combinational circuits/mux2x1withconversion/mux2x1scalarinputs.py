from myhdl import *

@block
def mux(z, a, b, sel):

    """ Multiplexer.

    z -- mux output
    a, b -- data inputs
    sel -- control input: select a if asserted, otherwise b

    """
    @always_comb
    def comb():
        if sel == 0:
            z.next = a
        else:
            z.next = b

    return comb

def convert():
    z, a, b, sel = [Signal(bool(0)) for i in range(4)]
    convInst = mux(z, a, b, sel)
    convInst.convert(hdl='Verilog')

convert()