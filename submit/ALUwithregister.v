module ALUwithregister(KEY, SW, HEX0, HEX4, HEX5, LEDR);
    input [0:0] KEY; // Controls the clock. Press it to reset the register. 
    input [9:0] SW; // SW[3:0] = Signal A, SW[7:5] = Signal B, SW[9] = reset_n
    output [6:0] HEX0;
    output [6:0] HEX4;
    output [6:0] HEX5;
    output [7:0] LEDR;
    #NOTICE: THERE IS NO INPUT FOR SW[4]!!!
  
  	//REGISTERS
  	reg [7:0] ALUout; // stores the output of the ALU
  	reg [7:0] register; // stores value of ALUout when clock is 1 (key not pressed)
  	
  	//WIRES
  	wire [4:0] oneplusa;
	wire [4:0] aplusb;

  	fourbitadder fa0(SW[3:0], 4'b0001, oneplusa[4:0]);
  	fourbitadder fa1(SW[3:0], register[3:0], aplusb[4:0]);

	//COMBINATIONAL CIRCUIT
	always @(*)
	begin
      case (SW[3:0])
        3'b000: ALUout[7:0] = {3'b000, oneplusa[4:0]};
        3'b001: ALUout[7:0] = {3'b000, aplusb[4:0]};
        3'b010: ALUout[7:0] = {3'b000, SW[3:0] + register[3:0]};
        3'b011: ALUout[7:0] = {SW[3:0] | register[3:0], {SW[3:0] ^ register[3:0]}};
        3'b100: ALUout[7:0] = {7'b0000000, (|{SW[3:0], register[3:0]})};
        3'b101: ALUout[7:0] = register[3:0] << SW[3:0];
        3'b110: ALUout[7:0] = register[3:0] >> SW[3:0];
        3'b111: ALUout[7:0] = register[3:0] * SW[3:0];
        default: ALUout[7:0] = 8'b00000000;
		endcase
	end
  	
  	//SEQUENTIAL CIRCUIT
  	always @(posedge KEY[0]) //clock input for register
    begin
      if (SW[9] == 1'b0)
        register[7:0] <= 8'b00000000; // reset the register (when key pressed)
      else
        register[7:0] <= ALUout[7:0]; // store ALU output value (key not pressed)
    end

  	assign LEDR[7:0] = ALUout[7:0]; // display ALU outputs on LEDR
  
  	hex_display hex0(.c(SW[3:0]), .hex(HEX0[6:0])); 	// HEX0 displays the value of Data (A) in hex
  	hex_display hex4(.c(ALUout[3:0]), .hex(HEX4[6:0])); // 
  	hex_display hex5(.c(ALUout[7:4]), .hex(HEX5[6:0])); // 
endmodule


module hex_display( input [3:0] c, output [6:0] hex);
  //ports are c (input) and hex (output)
  
  assign hex[6] =  c[3] & c[2] & ~c[1] & ~c[0] |
                  ~c[3] & ~c[2] & ~c[1] |
                  ~c[3] & c[2] & c[1] & c[0];

  assign hex[5] = ~c[3] & c[1] & c[0] |
                  ~c[3] & ~c[2] & c[0] |
                  ~c[3] & ~c[2] & c[1] |
                   c[3] & c[2] & ~c[1] & c[0];

  assign hex[4] = ~c[3] & c[0] |
                  ~c[2] & ~c[1] & c[0] |
                  ~c[3] & c[2] & ~c[1] |
                  ~c[3] & c[2] & ~c[1] & c[0] |
                  ~c[3] & c[2] & c[1] & c[0] |
                   c[3] & ~c[2] & ~c[1] & c[0];

  assign hex[3] = ~c[3] & ~c[2] & ~c[1] & c[0] |
                   c[2] & c[1] & c[0] |
                  ~c[3] & c[2] & ~c[1] & ~c[0] |
                   c[3] & ~c[2] & c[1] & ~c[0];

  assign hex[2] =  c[3] & c[2] & c[1] |
                   c[3] & c[2] & ~c[0] |
                  ~c[3] & ~c[2] & c[1] & ~c[0];

  assign hex[1] =  c[3] & c[1] & c[0] |
		 		   c[2] & c[1] & ~c[0] |
	          	   c[3] & c[2] & ~c[0] |
		 		  ~c[3] & c[2] & ~c[1] & c[0];

  assign hex[0] = ~c[3] & ~c[2] & ~c[1] & c[0] |
                  ~c[3] & c[2] & ~c[1] & ~c[0] |
                   c[3] & c[2] & c[1] & c[0];
endmodule


                               
module fourbitadder(input [3:0] A, input [3:0] B, output [4:0] LEDR);

    wire [2:0] conn;
	
  	fulladder fa0(
      	.a(A[0]), 
      	.b(B[0]), 
      	.cin(B[3]), 
		.s(LEDR[0]), 
      	.cout(conn[0])
		);

	fulladder fa1(
      	.a(A[1]), 
      	.b(B[1]), 
		.cin(conn[0]), 
		.s(LEDR[1]), 
		.cout(conn[1])
		);

	fulladder fa2(
      	.a(A[2]), 
      	.b(B[2]), 
		.cin(conn[1]), 
		.s(LEDR[2]), 
		.cout(conn[2])
		);

	fulladder fa3(
      	.a(A[3]), 
      	.b(B[3]), 
		.cin(conn[2]), 
		.s(LEDR[3]), 
		.cout(LEDR[4])
    	);
endmodule


module fulladder(
  	input a, b, cin, 
  	output s, cout
  	);
  
  	wire conn0, conn1, conn2;
    
	assign s = a^b^cin;
	assign cout = (a & b) | (cin & (a^b));
endmodule
