module tb_fa;

reg a;
reg b;
reg c;
wire sum;
wire co;

initial begin
    $from_myhdl(
        a,
        b,
        c
    );
    $to_myhdl(
        sum,
        co
    );
end

fa dut(
    a,
    b,
    c,
    sum,
    co
);

endmodule
