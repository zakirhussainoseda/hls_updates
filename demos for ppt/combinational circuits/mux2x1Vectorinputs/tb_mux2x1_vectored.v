module tb_mux2x1_vectored;

wire [7:0] y;
reg [7:0] a;
reg [7:0] b;
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

mux2x1_vectored dut(
    y,
    a,
    b,
    sel
);

endmodule
