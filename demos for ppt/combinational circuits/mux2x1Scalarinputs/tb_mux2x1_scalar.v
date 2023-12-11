module tb_mux2x1_scalar;

wire y;
reg a;
reg b;
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

mux2x1_scalar dut(
    y,
    a,
    b,
    sel
);

endmodule
