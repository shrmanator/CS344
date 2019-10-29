/* Freeing from the middle of an allocated block
 was a technical part of this assignment and
 involved multiple cases. I think the merge
 case is an interesting operation, so let's put
 throught the following test:
 
 The test will allocate some memory to partition.
 4 blocks are allocated. Then,
- the top block is freed
- the middle block is freed
- print results
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include "smalloc.h"

#define SIZE 4096 * 64

/* Simple test for smalloc and sfree. */

int main() {
    
    mem_init(SIZE);

    char *ptrs[10];

    ptrs[0] = smalloc(5);
    ptrs[1] = smalloc(10);
    ptrs[2] = smalloc(15);
    ptrs[3] = smalloc(4);
    write_to_mem(1000, ptrs[0], 0);
    write_to_mem(1000, ptrs[1], 1);
    write_to_mem(1000, ptrs[2], 2);
    write_to_mem(1000, ptrs[3], 3);

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
