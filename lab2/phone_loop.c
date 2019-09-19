#include <stdio.h>

int main() {
    char phone[11];
    int the_int;
    
    scanf("%s", phone);
    while (1) {
        scanf("%d", &the_int);

        if (the_int == -1) {
            printf("%s\n", phone);
        }
        else if (the_int >= 0 && the_int <= 9) {
            printf("%c\n", phone[the_int]);
        }
        else if (the_int < -1 || the_int > 9) {
            printf("ERROR\n");
        }
    }
    return 0;
}
