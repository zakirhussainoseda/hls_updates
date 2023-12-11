from myhdl import *

@block
def dff(q, d, clk,rst):

    @always(clk.posedge)
    def clk_logic():
        q.next = d

    return clk_logic
	
	@always(rst.posedge)
    def rst_logic():
        q.next = 0

    return rst_logic
