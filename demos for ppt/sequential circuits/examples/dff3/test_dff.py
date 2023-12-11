from myhdl import *
from random import randrange
from dff import dff
@block
def test_dff():

    q, d, clk, rst = [Signal(bool(0)) for i in range(3)]

    dff_inst = dff(q, d, clk, rst)

    @always(delay(10))
    def clkgen():
        clk.next = not clk
		
	@always(delay(100))
    def rstgen():
        rst.next = not rst

    @always(clk.negedge)
    def stimulus():
        d.next = randrange(2)

    return dff_inst, clkgen, stimulus


def simulate(timesteps):
    simInst = test_dff() 
    simInst.config_sim(trace=True, tracebackup=False)
    simInst.run_sim(timesteps, quiet=0) 

simulate(2000)

def convert():
    q, d, clk, rst= [Signal(bool(0)) for i in range(3)]
    convInst = dff(q, d, clk,rst)  #, 'Verilog')  
    convInst.convert(hdl='Verilog')
    convInst.convert(hdl='VHDL')

convert()