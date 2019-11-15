/* The purpose of this program is to practice writing signal handling
 * functions and observing the behaviour of signals.
 */

#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>

/* Message to print in the signal handling function. */
#define MESSAGE "%ld reads were done in %ld seconds.\n"

/* Global variables to store number of read operations and seconds elapsed. 
 */
long num_reads, seconds;

/*
 It's a handler.
 */
void handler(int code) {
    fprintf(stderr, "it ded");
    exit(0);
}

/* The first command-line argument is the number of seconds to set a timer to run.
 * The second argument is the name of a binary file containing 100 ints.
 * Assume both of these arguments are correct.
 */
int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: time_reads s filename\n");
        exit(1);
    }
    seconds = strtol(argv[1], NULL, 10);

    FILE *fp;
    if ((fp = fopen(argv[2], "r")) == NULL) {
      perror("fopen");
      exit(1);
    }
    
    struct sigaction siggy;
    siggy.sa_handler = handler;
    siggy.sa_flags = 0;             // default flags
    sigemptyset(&siggy.sa_mask);   // don't block signals during handler
    sigaction(SIGPROF, &siggy, NULL);
    
    /* In an infinite loop, read an int from a random location in the file,
     * and print it to stderr.
     */
    for (;;) {
        int j, value;
        j = random() % 100;
        fseek(fp, j * sizeof(int), SEEK_SET);
        value = read(fileno(fp), &value, 1);
        fprintf(stderr, "%d", value);
    }
    
    
    return 1; // something is wrong if we ever get here!
}
