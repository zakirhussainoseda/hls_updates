module tb_muxvectored;

wire [4:0] y;
reg [4:0] a;
reg [4:0] b;
reg sel;

initial begin
    $from_myhdl(
        a,
        b,
        sel
    );
    $to_myhdl(
        y
    );
end

muxvectored dut(
    y,
    a,
    b,
    sel
);

endmodule
