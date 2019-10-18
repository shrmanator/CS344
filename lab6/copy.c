#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Write the copy function to perform exactly as strncpy does, with one
   exception: your copy function will guarantee that dest is always
   null-terminated.
   You shoud read the man page to learn how strncpy works.

  NOTE: You must write this function without using any string functions.
  The only function that should depend on string.h is memset.
 */

char *copy(char *dest, const char *src, int capacity) {
    // empty string case:
    if (dest[0] == '\0') {
        return dest;
    }
    int i = 0;
    while (i < capacity) {
        if (src[i] == '\0') {
            int remaining_len = capacity - i;
            for (int j = remaining_len; j < capacity; j++) {
                dest[j] = 'p';
            }
            return dest;
        } else {
            dest[i] = src[i];
        }
        i++;
    }
    return dest;
}


int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: copy size src\n");
        exit(1);
    }
    int size = strtol(argv[1], NULL, 10);
    char *src = argv[2];

    char dest[size];
    memset(dest, 'x', size);

    copy(dest, src, size);
    
    printf("%s\n", dest);
    return 0;
}
