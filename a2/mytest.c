/* I found the most technical part of this assignment
 to be freeing from the middle blocks of memory. To test
 the logic, I have set up the following:
 
 This test will allocate 4 blocks of memory. Then,
- free the top block
- free the middle block
- print results
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include "smalloc.h"


/* Simple test for smalloc and sfree. */

int main() {
    
    mem_init(10);
    
    char *ptrs[4];
    int i;

    ptrs[0] = smalloc(10);
    ptrs[1] = smalloc(5);
    ptrs[2] = smalloc(5);
    ptrs[3] = smalloc(10);
    
    sfree(ptrs[0]);
    sfree(ptrs[2]);
    
    for(i = 0; i < 4; i++) {
        int num_bytes = (i+1) * 10;
        write_to_mem(num_bytes, ptrs[i], i);
    }
    
    
}
