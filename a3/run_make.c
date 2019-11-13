#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>

#include <time.h>
#include "pmake.h"

/* Returns Rule struct corresponding
*/ to target, or NULL if not exist.
Rule *get_target_rule(char *target, Rule *rules) {
    Rule *curr = rules;
    while (curr !=NULL) {
        if (strcmp(curr->target, target) == 0) {
            return curr;
        }
        curr = curr->next_rule;
    }
    return NULL;
}

/* Returns 1 if dep newer
*/ than target, 0 otherwise.
int dep_newer_than_target() {
    
}


execute_all_actions(Rule *rules) {
    struct stat sb;
    printf("Last file modification:   %s", ctime(&sb.st_mtime));
    }
}


// ====  end helpers ====


void run_make(char *target, Rule *rules, int pflag) {
    // TODO
    if (target == NULL || dep_newer_than_target(target, rules)) {
        execute_all_actions(rules);
    } else {
        Rule *rule = get_target_rule(target, rules);
    }
}

