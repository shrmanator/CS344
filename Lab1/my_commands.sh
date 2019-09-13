./echo_arg csc209 > echo_out.txt 
./echo_stdin < echo_stdin.c
./count 210 > echo_out.txt 
wc -c < echo_out.txt  
ls -S | head -1 < ./echo_stdin
