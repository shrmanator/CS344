#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define MAXLINE 256

#define SUCCESS "Password verified\n"
#define INVALID "Invalid password\n"
#define NO_USER "No such user\n"

int main(void) {
    char user_id[MAXLINE];
    char password[MAXLINE];

    /* The user will type in a user name on one line followed by a password
    on the next.
    DO NOT add any prompts.  The only output of this program will be one
    of the messages defined above.
    */

    if(fgets(user_id, MAXLINE, stdin) == NULL) {
        perror("fgets");
        exit(1);
    }
    if(fgets(password, MAXLINE, stdin) == NULL) {
        perror("fgets");
        exit(1);
    }

    // TODO
    
    pid_t pid = fork();
    
    if (pid == 0) {
        int filefd = open("pass.txt", O_RDWR | S_IRWXU | O_TRUNC);
            if (filefd == -1) {
                perror("open");
            }
        if (dup2(filefd, fileno(stdout)) == -1) {
            perror("dup2");
        }
        close(filefd);
        execlp("./validate", NULL);
        perror("exec");
        exit(1);
    }
    else if (pid < 0){
        perror("fork");
        exit(1);
    }
    else {
        int status = wait(pid);
        if (wait(&status) != -1) {
            if (WIFEXITED(status)) {
                fprintf(stderr, "Process exited with %d\n",
                        WEXITSTATUS(status));
            } else {
                fprintf(stderr, "Process teminated\n");
            }
        }
    } else {
        perror("fork");
        exit(1);
    }
    return 0;
}
