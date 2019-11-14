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
 Returns last time rule was modified.
 */
struct timespec last_modified_time(char *path) {
    struct stat attr;
    if (stat(path, &attr) == 0) {
        return attr.st_mtime;
    }
    struct timespec ti;
    return ti;
}

/*
 Returns 1 if t2 is modified more recently,
 0 otherwise.
*/
int compare_times(time_t t1, time_t t2) {
    if (t1.tv_secs > t2.tv_secs) {
        // t1 older than t2
        return 1;
    }
    if (t1.tv_secs < t2.tv_secs) {
        return 0;
    }
    if (t1.tv_nsecs > t2.tv_nsecs) {
        // t1 older than t2 in nano
        return 1;
    }
    return 0;
}
    
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
Execute given action
*/
void execute_action(Action *act) {
    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        kill(get_ppid(), STDIN)
        exit(1);
    }
    if (pid == 0) {
        execvp(act->actions[0], act->actions);
    }
    if (pid > 0) {
        wait(get_ppid());
    }
}


/*
Recursively evaluate
each dependency rule.
*/
void evaluate_rule(Rule *rule, struct timespec parent_time) {
    struct timespec last_mtime = last_modified_on(rule);
    
    if (compare_times(parent_time, last_mtime)) {
        return; // no rebuild
    }
    Dependency *dep = rule->dependencies;
    while (dep != NULL) {
        evaluate_rule(dep->rule, last_mtime);
        dep = dep->next_dep;
    }
    
    Action *act = rule->actions;
    while (act != NULL) {
        execute_action(act);
        act = act->next_act;
    }
}


// ====  end helpers ====


void run_make(char *target, Rule *rules, int pflag)
{
    Rule *rule = rules;
    if (target != NULL) {
        rule = get_rule(target, rules);
    }
    evaluate_rule(rule, last_modified_time(rule)); // evaluates first rule
}
