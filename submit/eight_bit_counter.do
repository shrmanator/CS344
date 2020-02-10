 vlib work

vlog -timescale 1ns/1ns eight_bit_counter.v

vsim eight_bit_counter

log {/*}
add wave {/*}

force {SW[0]} 1 0, 0 1 // reset circuit board to 0s
force {KEY[0]} 1 10, 0 20// start the clock after board is reset
force {SW[1]} 1 10, 0 20 - repeat 2
run 100ns