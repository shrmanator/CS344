Last login: Mon Feb  3 13:53:50 on ttys000
doventerprise@Dovs-MacBook-Pro ~ % ssh -Y sherma73@teach.cs.utoronto.ca
sherma73@teach.cs.utoronto.ca's password: 
Permission denied, please try again.
sherma73@teach.cs.utoronto.ca's password: 
Permission denied, please try again.
sherma73@teach.cs.utoronto.ca's password: 
    Type "faq" to view FAQ, and "rules" to view usage policy.
    Report system problems by sending email to <sysadmin@teach.cs.toronto.edu>.

The Teaching Labs are: BA2200 BA2210 BA2220 BA2240 BA2270 BA3175 BA3185 BA3195 BA3200

This is a shared Linux system. By using this system, you acknowledge that
some information about your computer account (e.g. login name, process data,
etc.) will be available to other users sharing this system, in ways 
typical of shared Linux systems.  

Last login: Mon Feb  3 13:54:03 2020 from public-243-125.nat.utoronto.ca
wolf:~$ cd ~/Desktop
wolf:~/Desktop$ ls
ALUwithregister.do  DovCloud  transcript  wlft8VuM7j
ALUwithregister.v   misc.     vsim.wlf    work
wolf:~/Desktop$ vim shiftregister8bit.v




















wolf:~/Desktop$ vsim
Reading pref.tcl
wolf:~/Desktop$ vim shiftregister8bit.do
wolf:~/Desktop$ vim shiftregister8bit.do
wolf:~/Desktop$ vsim
Reading pref.tcl

^[[A^[[B^?^?^?^?^?

XIO:  fatal IO error 0 (Success) on X server "localhost:24.0"
      after 23459 requests (22892 known processed) with 1285 events remaining.
** Fatal: Read failure in vlm process (0,0)
wolf:~/Desktop$ 
wolf:~/Desktop$ 
wolf:~/Desktop$ 
wolf:~/Desktop$ vim shiftregister8bit.v
kjj


wolf:~/Desktop$ vsim
Reading pref.tcl
wolf:~/Desktop$ vim shiftregister8bit.v
wolf:~/Desktop$ vsim
Reading pref.tcl
wolf:~/Desktop$ vim shiftregister8bit.do
wolf:~/Desktop$ vsim
Reading pref.tcl
:^?wolf:~/Desktop$ vim shiftregister8bit.v
wolf:~/Desktop$ vsim
Reading pref.tcl
&
wolf:~/Desktop$ &
-bash: syntax error near unexpected token `&'
wolf:~/Desktop$ vim shiftregister8bit.v
wolf:~/Desktop$ vsim &
[1] 11247
wolf:~/Desktop$ Reading pref.tcl

[1]+  Done                    vsim
wolf:~/Desktop$ 
wolf:~/Desktop$ 
wolf:~/Desktop$ vim shiftregister8bit.v

module shiftregister8bit(SW, KEY, LEDR);
        input [9:0] SW;                 // SW[7:0] are inputs to LoadVal[7:0]. SW[9] is reset_n (SW[8] not used).
        input [3:0] KEY;                // KEY[0] clk, KEY[1] load_n, KEY[2] ShiftRight, KEY[3] ASR
        output [7:0] LEDR;              // output of ShiftBit instances 0-7


        // WIRING
        wire [7:0] LoadVal;     //LoadVal: connected to load_val input of each ShifterBit instance
        assign LoadVal[7:0] = SW[7:0];

        wire reset_n;
    assign reset_n = SW[9];

        wire clk;
        assign clk = KEY[0];

        wire load_n;
        assign load_n = KEY[1];

        wire ShiftRight;
        assign ShiftRight = KEY[2];

        wire ASR;
        assign ASR = KEY[3];

        wire [8:0] Q;                   // an array of 8 bits + extra input bit (ignore) of each shifterbit instance


    // perform sign-extension when the signal ASR is high or load zeros if ASR is low.
        mux2to1 mux(.x(1'b0),
                            .y(Q[7]),
                            .s(ASR),
                .m(Q[0])
                                );

        // CONNECTING SHIFTERBITS
    ShifterBit sb0(.loadval(LoadVal[0]),
                   .in(Q[0]),
                   .out(Q[1]),
                   .shift(ShiftRight),
                   .load_n(load_n),
                   .clk(clk),
                   .reset_n(reset_n)
"shiftregister8bit.v" 162L, 4043C                                                                                 23,2-9        Top
