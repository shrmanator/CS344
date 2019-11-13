#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>

#include "pmake.h"

/* Print the list of actions */
void print_actions(Action *act) {
    while(act != NULL) {
        if(act->args == NULL) {
            fprintf(stderr, "ERROR: action with NULL args\n");
            act = act->next_act;
            continue;
        }
        printf("\t");

        int i = 0;
        while(act->args[i] != NULL) {
            printf("%s ", act->args[i]) ;
            i++;
        }
        printf("\n");
        act = act->next_act;
    }
}

/* Print the list of rules to stdout in makefile format. If the output
   of print_rules is saved to a file, it should be possible to use it to
   run make correctly.
 */
void print_rules(Rule *rules){
    Rule *cur = rules;
    
    while(cur != NULL) {
        if(cur->dependencies || cur->actions) {
            // Print target
            printf("%s : ", cur->target);
            
            // Print dependencies
            Dependency *dep = cur->dependencies;
            while(dep != NULL){
                if(dep->rule->target == NULL) {
                    fprintf(stderr, "ERROR: dependency with NULL rule\n");
                }
                printf("%s ", dep->rule->target);
                dep = dep->next_dep;
            }
            printf("\n");
            
            // Print actions
            print_actions(cur->actions);
        }
        cur = cur->next_rule;
    }
}

//Returns Rule of the corresponding target:
Rule *get_rule(char *target, Rule *rules);

//Returns input line's target (if one exists):
char *parse_target(char *line) {
    char *target = malloc(500);
    for (int i = 0; line[i] != '\0'; i++) {
        if (line[i] == ':' || line[i] == ' ') {
            break;
        } else {
            target[i] = line[i];
            target[i + 1] = '\0';
        }
    }
    return target;
}

// an array of pointers to null-terminated strings that
// represent the argument list available to the new program.
Action *parse_action(char *lines) {
    int max_array_size = 256;
    lines = lines + 1;
    
    char *curr1;
    // create action:
    Action *action = malloc(sizeof(Action));
    action->args = malloc(max_array_size);
    // insert action strings:
    int i = 0;
    while((curr1 = strsep(&lines, " ")) != NULL ) {
        action->args[i++] = strdup(curr1);
    }
    action->args[i] = NULL;
    action->next_act = NULL;
    return action;
}

// populate each rule in rules with their dependencies:
// the function:
// 1. creates a linked-list of Dependencies
// 2. returns that linked-list
Dependency *parse_dependencies(char *line, Rule *rules) {
    char *dep_target;
    printf("line is %s\n", line);
    
    int coln_index;
    for (coln_index = 0; line[coln_index] != ':' && line[coln_index] != '\0'; coln_index++) {}

    line += coln_index + 2; // + 2 counts for whitespace.
    Dependency *first = NULL, *previous = NULL;
    
    while ((dep_target = strsep(&line, " ")) != NULL) {
        Dependency *new_dep = malloc(sizeof(Dependency));
        new_dep->rule = get_rule(dep_target, rules);
        printf("got rule %p from target %s", new_dep->rule, dep_target);
        
        new_dep->next_dep = NULL;
        if (first == NULL) {
            first = new_dep;
        } else {
            previous->next_dep = new_dep;
        }
        previous = new_dep;
    }
    return first;
}


/* Create the rules data structure and return it.
   Figure out what to do with each line from the open file fp
     - If a line starts with a tab it is an action line for the current rule
     - If a line starts with a word character it is a target line, and we will
       create a new rule
     - If a line starts with a '#' or '\n' it is a comment or a blank line
       and should be ignored.
     - If a line only has space characters ('', '\t', '\n') in it, it should be
       ignored.
 */
Rule *parse_file(FILE *fp) {
    // don't forget to free Rule in main!
    if(fp == NULL) {
        perror("Error opening file");
        exit(1);
    }
    char line[256];
    Rule *first = NULL, *prev = NULL, *new_rule = NULL;
    
    while (fgets(line, sizeof(line), fp)) {
        if (is_comment_or_empty(line)) {
            continue;
        }
        if (line[0] == '\t') {
            // line is a single action:
            prev->actions = parse_action(line);
        } else {
            new_rule = malloc(sizeof(Rule));
            new_rule->next_rule = NULL;
            new_rule->actions = NULL;
            new_rule->target = parse_target(line);
            if (first == NULL) {
                    first = new_rule;
            } else if (prev != NULL) {
                    prev->next_rule = new_rule;
            }
            prev = new_rule;
        }
    }
    Rule *curr = first;
    fseek(fp, 0, SEEK_SET);
    while (fgets(line, sizeof(line), fp)) {
        if (is_comment_or_empty(line)) {
            continue;
        }
        if (line[0] == '\t') {
            // line is a single action:
            continue;
        }
        curr->dependencies = parse_dependencies(line, first);
        curr = curr->next_rule;
    }
    fclose(fp);
    return first;
}

int main() {
    FILE *file = fopen("Makefile2" ,"r");
    print_rules(parse_file(file));
}
