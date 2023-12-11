module tb_ha;

reg a;
reg b;
wire sum;
wire co;

initial begin
    $from_myhdl(
        a,
        b
    );
    $to_myhdl(
        sum,
        co
    );
end

ha dut(
    a,
    b,
    sum,
    co
);

endmodule
