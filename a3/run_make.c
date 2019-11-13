#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>

#include <time.h>
#include "pmake.h"

/*
 Returns creation time of rule in millisecs.
 */
//char *get_last_modified_time(char *rule) {
//    struct stat attr;
//    stat(path, &attr);
//    return ctime(&attr.st_mtime));
//}
//
//Rule *get_rule(char *target, Rule *rules) {
//    Rule *curr = rules;
//    while (curr !=NULL) {
//        if (strcmp(curr->target, target) == 0) {
//            return curr;
//        }
//        curr = curr->next_rule;
//    }
//    return NULL;
//}
//
///* Returns 1 if dep newer
//*/ than target, 0 otherwise.
//int dep_newer_than_target(char *target, Rule *deps) {
//    char *dep_date; // last time dependency was modified
//    char *target_date = get_last_modified_time(get_rule(target));
//
//    Rule *curr;
//    while (curr != NULL) {
//        dep_date = get_last_modified_time(get_rule(curr));
//        if (difftime(target_mod_date, dep_mod_date) < 0) {
//            return 1;
//        }
//        curr = curr->next_rule;
//    }
//    return 0;
//}
//
//








/*
Recursively evaluate
each dependency rule.
*/
int update_dependencies(Rule *dep) {
    if (dep != NULL)
        update_dependencies(dep->next_dep);
    return 0;
}


// ====  end helpers ====


void run_make(char *target, Rule *rules, int pflag)
{
    if (target == NULL) {
        update_dependencies(rules->dependencies);
    } else {
        Rule *rule = get_rule(target, rules);
        update_dependencies(rule->dependencies);
    }
}
