from myhdl import *

@block
def dffa(q, d, clk, rst):

    @always_seq(clk.posedge, reset=rst)
    def logic():
        if rst == 0:    # nRst ?  or use active high ?
            q.next = 0
        else:
            q.next = d

    return logic
