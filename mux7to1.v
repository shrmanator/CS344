module mux(LEDR, SW);
  input SW;
  output LEDR;

  mux7to1 u0(
    .Input(SW[6:0]), // first 6 switches on DE1 board
    .MuxSelect(SW[9:7]), // last 3 switches on DE1 board
    .Output(LEDR[0]) // that LED right above SW[0]
    );
endmodule

module mux7to1(Input, MuxSelect, Output);
  input [6:0] Input;
  input [2:0] MuxSelect; 
  output Output; // 

  reg Out;

  always @(∗) begin
    case (MuxSelect [2:0]) 
      3'b000: Out = Input[0]; 
      3'b001: Out = Input[1]; 
      3'b010: Out = Input[2]; 
      3'b011: Out = Input[3];
      3'b100: Out = Input[4];
      3'b101: Out = Input[5];
      3'b110: Out = Input[6];
      default : Out = 1'b0;
    endcase 
  end

  assign Output = Out;
endmodule