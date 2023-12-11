module tb_orgate;

reg a;
reg b;
wire y;

initial begin
    $from_myhdl(
        a,
        b
    );
    $to_myhdl(
        y
    );
end

orgate dut(
    a,
    b,
    y
);

endmodule
