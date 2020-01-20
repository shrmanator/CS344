module display(HEX0, SW);
    input [9:0] SW;
    output [6:0] HEX0;

    hex_display u0(
        .hex(HEX0),
   	.c(SW[3:0])
	);
endmodule

module hex_display(hex, c);
  input [3:0] c;
  output [6:0] hex;
  
  assign hex[6] = c[2] & ~c[1] & ~c[0] | ~c[3] & ~c[2] & ~c[1] | ~c[3] & c[2] & c[1] & c[0];
  assign hex[5] = ~c[3] & ~c[2] & c[0] | ~c[3] & ~c[2] & c[1] | ~c[3] & c[1] & c[0] | c[3] & c[2] & ~c[1]& c[0];
  assign hex[4] = ~c[3] & c[2] & ~c[1] | ~c[3] & ~c[1] & c[0] | ~c[3] & c[1] & c[0] | c[3] & ~c[2] & ~c[1] & c[0];
  assign hex[3] = ~c[3] & ~c[1] & c[0] & ~c[3] & c[2] & c[0] | c[2] & c[1] & c[0] | c[3] & ~c[2] & c[0];
  assign hex[2] = c[3] & c[2] & ~c[1] & ~c[0] | ~c[3] & ~c[2] & c[1] & ~c[0] | c[3] & c[2] & c[1];
  assign hex[1] = ~c[3] & c[2] & ~c[1] & c[0] | c[2] & c[1] & ~c[0] | c[3] & c[2] & c[1] | c[3] & c[1] & c[0] & c[3] & c[2] & ~c[1] & ~c[0];
  assign hex[0] = ~c[3] & c[2] & c[1] & ~c[0] | ~c[3] & ~c[2] & ~c[1] & c[0] | c[3] & ~c[2] & c[1] & c[0] | c[1] & c[0] & c[1] & ~c[0];
endmodule