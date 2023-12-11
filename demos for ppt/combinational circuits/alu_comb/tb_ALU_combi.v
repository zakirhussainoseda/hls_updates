module tb_ALU_combi;

wire [15:0] q;
wire o;
wire z;
wire n;
reg [15:0] a;
reg [15:0] b;
reg [3:0] f;

initial begin
    $from_myhdl(
        a,
        b,
        f
    );
    $to_myhdl(
        q,
        o,
        z,
        n
    );
end

ALU_combi dut(
    q,
    o,
    z,
    n,
    a,
    b,
    f
);

endmodule
