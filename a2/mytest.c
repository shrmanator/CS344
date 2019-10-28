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
    
    mem_init(1000);

    char *ptrs[10];

    ptrs[0] = smalloc(5);
    ptrs[1] = smalloc(5);
    ptrs[2] = smalloc(5);
    ptrs[3] = smalloc(5);
    write_to_mem(10, ptrs[0], 0);
    write_to_mem(10, ptrs[1], 1);
    write_to_mem(10, ptrs[2], 2);
    write_to_mem(10, ptrs[3], 3);

    sfree(ptrs[0]);
    sfree(ptrs[2]);
    
    printf("List of allocated blocks:\n");
    print_allocated();
    printf("List of free blocks:\n");
    print_free();
    printf("Contents of allocated memory:\n");
    print_mem();
    
    printf("freeing %p result = %d\n", ptrs[1], sfree(ptrs[1]));
    
    printf("List of allocated blocks:\n");
    print_allocated();
    printf("List of free blocks:\n");
    print_free();
    printf("Contents of allocated memory:\n");
    print_mem();

    mem_clean();
    return 0;
}
