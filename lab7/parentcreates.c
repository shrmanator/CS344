#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int i;
    int iterations;

    if (argc != 2) {
        fprintf(stderr, "Usage: forkloop <iterations>\n");
        exit(1);
    }
    
    pid_t cur_process = getppid();
    int exit_value;
    iterations = strtol(argv[1], NULL, 10);
    
    for (int i = 0; i < iterations; i++) {
        if (cur_process == getppid()) {
            if ((cur_process = fork()) == -1) {
                perror("fork");
                exit(1);
            }
            wait(&exit_value);
        }
        printf("ppid = %d, pid = %d, i = %d\n", getppid(), getpid(), i);
    }
    return 0;
}
