module morse_code_circuit(SW, KEY, LEDR, CLOCK_50);
  	input [2:0] SW; //three_bit_binary_of_letter
	input CLOCK_50;
  	input [1:0] KEY; 	//KEY[1]: load_pattern_into_register, KEY[0]: reset_to_000
  	output [0:0] LEDR; // led_output
	
	morse_output m0(SW[2:0], KEY[1], CLOCK_50, KEY[0], LEDR[0], 1'b1);
endmodule


// translates to morse code
module morse_output(key, start, clk, asr_n, out, rate);
	input [2:0] key;
	input start, asr_n, rate, clk;
	output out;
	
	wire [13:0] letter;
	wire [24:0] rdval;
	wire shift_enable;
	wire [24:0] countdown;
	
	reg rdenable, par_load;
	
	always @(negedge start, negedge asr_n)
	begin
		if (asr_n == 0)
			begin
			par_load <= 1;
			rdenable <= 0;
			end
		else if (start == 0)
			begin
			par_load <= 0;
			rdenable <= 1'b1;
			end
	end
	
	
	assign countdown = (rate == 1) ? 25'd24999999 : 25'd3;
	
	LUT LUT0(key, letter);
	
	rate_divider rd0(rdenable, countdown, clk, asr_n, rdval);
	
	assign shift_enable = (rdval == 0) ? 1 : 0;
	
	shift_register s0(shift_enable, letter, par_load, asr_n, clk, out);

endmodule


module shift_register(enable, load, par_load, asr_n, clk, out);
	input enable, par_load, asr_n, clk;
	input [13:0] load;
	output reg out;
	
	reg [13:0] q;
	
	always @(posedge clk, negedge asr_n)
	begin
		if (asr_n == 0)
			begin
			out <= 0;
			q <= 14'b0;
			end
		else if (par_load == 1)
			begin
			out <= 0;
			q <= load;
			end
		else if (enable == 1)
			begin
			out <= q[0];
			q <= q >> 1'b1;
			end
	end

endmodule


module LUT(
  input [2:0] in, // SW[2:0]
  output reg [13:0] out // 14-bit representation of morris code letter
  );
  
  always @(*)
	begin
      case(in)
        3'b000: out = 14'b10101000000000; // 0
        3'b001: out = 14'b11100000000000; // 1
        3'b010: out = 14'b10101110000000; // 2
        3'b011: out = 14'b10101011100000; // 3
        3'b100: out = 14'b10111011100000; // 4
        3'b101: out = 14'b11101010111000; // 5
        3'b110: out = 14'b11101011101110; // 6
        3'b111: out = 14'b11101110101000; // 7
        default: out = 14'b00000000000000;
      endcase
    end
endmodule


module rate_divider(enable, load, clk, asr_n, q);
	input enable, clk, asr_n;
	input [24:0] load;
	output reg [24:0] q;
	
	always @(posedge clk, negedge asr_n)
	begin
		if (asr_n == 1'b0)
			q <= load;
		else if (enable == 1'b1)
			begin
				if (q == 0)
					q <= load;
				else
					q <= q - 1'b1;
			end
	end
endmodule
