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

char *parse_target(char *line) {
    char *target = malloc(500);
    for (int i = 0; line[i] != '\0'; i++) {
        if (line[i] == ':' || line[i] == ' ') {
            return;
        } else {
            target[i] = line[i];
            target[i + 1] = '\0';
        }
    }
    return target;
}

void parse_action(Rule *rule, char *line) {
    printf("%s", line);
    rule->actions = malloc(sizeof(Action));
    if (line[0] == '.' && line[1] == '/') {
        rule->actions = line;
    }
}

Rule *get_rule(char *target, Rule *rules) {
    Rule *curr = rules;
    while (curr !=NULL) {
        if (strcmp(curr->target, target) == 0) {
            return curr;
        }
        curr = curr->next_rule;
    }
    return NULL;
}

Dependency *parse_dependencies(char *line, Rule *rules) {
    int coln_index;
    for (coln_index = 0; line[coln_index] != ':' && line[coln_index] != '\0'; i++) {}
    char *curr;
    Dependency *first = NULL;
    Dependency *previous = NULL;
    while ((curr = 1) != NULL) {
        Dependency *dep = malloc(sizeof(Dependency));
        dep->next_rule = NULL;
        dep->rule = get_rule(curr, rules);
        if (first == NULL) {
            first = dep;
        } else {
            previous->next_rule = dep;
        }
        previous = dep;
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
    Rule *new_rule = malloc(sizeof(Rule));
    while (fgets(line, sizeof(line), fp)) {
        if (line[0] != '#' && line[0] != ' ') {
            if (line[0] == '\t') {
                add_action(new_rule, line);
            }
            else {
                //add target to new_rule->target:
                add_target(new_rule, line);
                //create and populate next Rule:
                Rule *next_rule = malloc(sizeof(Rule));
                new_rule->next_rule = next_rule;
            }
        }
    }
    fclose(fp);
    return new_rule;
}



int main() {
    FILE *file = fopen("/Users/DovSherman/Desktop/sherma73/a3/Makefile", "r");
    Rule *rule = parse_file(file);
    while (rule != NULL) {
        printf("%s", rule->target);
        rule = rule->next_rule;
    }
}
