#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "pmake.h"

#define MAX_ARGS 32
#define MAX_NAME 128

/* Create an array of arguments suitable for passing into execvp 
   from "line". line is expected to start with a tab and contain a
   action from a Makefile. Remember to ensure that the last element
   of the array is NULL.

   It is fine to use MAX_ARGS to allocate enough space for the arguments
   rather than iterating through line twice. You may want to use strtok to
   split the line into separate tokens.

   Return NULL if there are only spaces and/or tabs in the line. No memory
   should be allocated and the return value will be NULL.
 */

char **build_args(char *line) {
    
    // TODO
    return NULL;
}

/* Return 1 if the line contains only spaces or a comment (#)
   Return 0 if the line contains any other character before a #

   We want to ignore empty lines or lines that contain only a comment.  This
   helper function identifies such lines.
 */
int is_comment_or_empty(char *line) {
    
    for(int i = 0; i < strlen(line); i++){
        if(line[i] == '#') {
            return 1;
        }
        if(line[i] != '\t' && line[i] != ' ') {
            return 0;
        }
    }
    return 1;
}

/* Convert an array of args to a single space-separated string in buffer.
   Returns buffer.  Note that memory for args and buffer should be allocted
   by the caller.
 */
char *args_to_string(char **args, char *buffer, int size) {
    buffer[0] = '\0';
    int i = 0;
    while(args[i] != NULL) {
        strncat(buffer, args[i], size - strlen(buffer));
        strncat(buffer, " ", size - strlen(buffer));
        i++;
    }
    return buffer;
}

Rule *get_rule(char *target, Rule *rules) {
    Rule *curr = rules;
    while (curr !=NULL) {
        if (strcmp(curr->target, target) == 0) {
            return curr;
        }
        curr = curr->next_rule;
    }
    curr = rules;
    while (curr->next_rule !=NULL) {
        curr = curr->next_rule;
    }
    Rule *new_rule = malloc(sizeof(Rule));
    new_rule->target = strdup(target);
    new_rule->dependencies = NULL;
    new_rule->actions = NULL;
    curr->next_rule = new_rule;
    new_rule->next_rule = NULL;
    return new_rule;
}
