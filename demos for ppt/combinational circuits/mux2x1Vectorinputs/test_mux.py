import random
from myhdl import block, instance, Signal, intbv, delay
from mux import mux

random.seed(5)
randrange = random.randrange

@block
def test_mux():

    z, a, b, sel = [Signal(intbv(0)) for i in range(4)]

    mux_1 = mux(z, a, b, sel)

    @instance
    def stimulus():
        print("z a b sel")
        for i in range(12):
            a.next, b.next, sel.next = randrange(8), randrange(8), randrange(2)
            yield delay(10)
            print("%s %s %s %s" % (z, a, b, sel))

    return mux_1, stimulus
'''
# The following is to run the simulation
tb = test_mux()
tb.run_sim()
'''
'''
# The following is to run the simulation and also for vcd file generation
def simulate(timesteps):
    simInst = test_mux() 
    simInst.config_sim(trace=True, tracebackup=False)
    simInst.run_sim(timesteps, quiet=0) 

simulate(2000)
'''
'''
# The following is to conversion to verilog and vhdl 
def convert():
    z, a, b, sel = [Signal(bool(0)) for i in range(4)]
    convInst = mux(z, a, b, sel)  #, 'Verilog')  
    convInst.convert(hdl='Verilog')
    convInst.convert(hdl='VHDL')

convert()
'''
