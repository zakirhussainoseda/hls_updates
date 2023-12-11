from myhdl import block, always_comb, Signal

@block
def mux2x1_scalar(y, a, b, sel):

    """ 
    Multiplexer

    y -- scalar data output
    a, b -- scalar data inputs
    sel -- control input: select a if asserted, otherwise b

    """

    @always_comb
    def comb():
        if sel == 1:
            y.next = b
        else:
            y.next = a

    return comb

def convert():
    y,a,b,sel = [Signal(bool(0)) for i in range(4)]
    convInst = mux2x1_scalar(y, a, b, sel)
    convInst.convert(hdl='Verilog')

convert()