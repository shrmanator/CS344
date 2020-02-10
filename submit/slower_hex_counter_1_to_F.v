module slower_hex_counter_1_to_F(SW, HEX0, CLOCK_50);
  input [3:0] SW; // SW[0] & SW[1]: rate selection, SW[2]: reset_n
  output [3:0] LEDR; // display output in binary
  output [6:0] HEX0; // display output in base-10
  input CLOCK_50;
  wire enable;
  reg [27:0] count;
  
  always @(*)
	begin
		case (SW[1:0])
			2'b00: count[27:0] = 28'd0;
			2'b01: count[27:0] = 28'd49999999;
			2'b10: count[27:0] = 28'd99999999;
			2'b11: count[27:0] = 28'd199999999;
			default: count[27:0] = 28'd0;
		endcase
	end
  
  RateDivider rd(.clk(CLOCK_50), .reset_n(SW[2]), .enable(enable), .d(count[27:0]));
  DisplayCounter dc(.clk(CLOCK_50), .reset_n(SW[2]), .enable(enable), .out(LEDR[3:0]));
  hexDecoder hd(.SW(LEDR[3:0]), .HEX(HEX0[6:0]));
  
endmodule


module DisplayCounter(clk, reset_n, enable, out);
	input clk, enable, reset_n;
  	output [3:0] out;
	reg [3:0] Q;
  
	always @(posedge clk)
	begin
      if(!reset_n)
			Q <= 0;
      	else if(enable == 1'b1) // if enable is high, increment by 1
			Q <= Q + 1'b1;
      	else if(enable == 1'b0) // else, keep the current state
			Q <= Q;
	end
endmodule


module RateDivider(clk, reset_n, enable, d);
	input [27:0] d;
	input reset_n;
	input clk;
	output enable;
  	reg [27:0] d_temp;
	reg [27:0] count;

  	always @(posedge clk, negedge reset_n)
	begin
		if (reset_n == 1'b0)
			count[27:0] <= d[27:0];
		else if (count[27:0] == 28'd0)
			count[27:0] <= d[27:0];
		else if (d[27:0] != d_temp[27:0])
			begin
				count[27:0] <= d[27:0];
				d_temp[27:0] <= d[27:0];
			end
		else
			count[27:0] <= count[27:0] - 28'd1;
	end
	assign enable = (count[27:0] == 28'd0) ? 1'b1 : 1'b0;
endmodule

module hexDecoder (SW, HEX);
	input [3:0] SW;
	reg [6:0] result;
	output [6:0] HEX;
	always @(*)
	begin
		case (SW[3:0])
			4'b0000: result[6:0] = 7'b1000000;
			4'b0001: result[6:0] = 7'b1111001;
			4'b0010: result[6:0] = 7'b0100100;
			4'b0011: result[6:0] = 7'b0110000;
			4'b0100: result[6:0] = 7'b0011001;
			4'b0101: result[6:0] = 7'b0010010;
			4'b0110: result[6:0] = 7'b0000010;
			4'b0111: result[6:0] = 7'b1111000;
			4'b1000: result[6:0] = 7'b0000000;
			4'b1001: result[6:0] = 7'b0010000;
			4'b1010: result[6:0] = 7'b0001000;
			4'b1011: result[6:0] = 7'b0000011;
			4'b1100: result[6:0] = 7'b1000110;
			4'b1101: result[6:0] = 7'b0100001;
			4'b1110: result[6:0] = 7'b0000110;
			4'b1111: result[6:0] = 7'b0001110;
			default: result[6:0] = 7'b1000000;
		endcase
	end
	assign HEX[6:0] = result[6:0];
endmodule