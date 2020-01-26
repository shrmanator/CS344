# Set the working dir, where all compiled Verilog goes.
vlib work

# Compile all Verilog modules in mux.v to working dir;
# could also have multiple Verilog files.
# The timescale argument defines default time unit
# (used when no unit is specified), while the second number
# defines precision (all times are rounded to this value)
vlog -timescale 1ns/1ns mux.v

# Load simulation using mux as the top level simulation module.
vsim mux

# Log all signals and add some signals to waveform window.
log {/*}
# add wave {/*} would add all items in top level simulation module.
add wave {/*}

# First test case
# Set input values using the force command, signal names need to be in {} brackets.
#force {SW[0]} 0
#force {SW[1]} 0
#force {SW[9]} 0
# Run simulation for a few ns.
#run 10ns
force {SW[0]} 0 0, 1 10ns -repeat 512
force {SW[1]} 0 0, 1 20ns -repeat 256
force {SW[2]} 0 0, 1 40ns -repeat 128
force {SW[3]} 0 0, 1 80ns -repeat 64
force {SW[4]} 0 0, 1 160ns -repeat 32
force {SW[5]} 0 0, 1 320ns -repeat 16
force {SW[6]} 0 0, 1 640ns -repeat 8
force {SW[7]} 0 0, 1 1280ns -repeat 4
force {SW[8]} 0 0, 1 2560ns -repeat 2
force {SW[9]} 0 0, 1 5120ns -repeat 1