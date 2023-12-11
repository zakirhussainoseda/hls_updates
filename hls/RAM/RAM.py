import myhdl
from myhdl import *
@block
def RAM(dout, din, addr, we, clk, depth=128):
    """ Ram model """
    mem = [Signal(intbv(0)[8:]) for i in range(depth)]

    @always(clk.posedge)
    def write():
        if we:
            mem[addr].next = din

    @always_comb
    def read():
        dout.next = mem[addr]

    return instances()
	
dout = Signal(intbv(0)[8:])
dout_v = Signal(intbv(0)[8:])
din = Signal(intbv(0)[8:])
addr = Signal(intbv(0)[7:])
we = Signal(bool(0))
clk = Signal(bool(0))
	
inst = RAM(clk=clk, addr=addr, we=we, din=din, dout=dout)
inst.convert(hdl="VHDL")
inst.convert(hdl="Verilog", testbench=False)