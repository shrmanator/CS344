#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/mman.h>
#include "smalloc.h"


// mem stores the starting address of the memory region that is reserved by mem_init.
void *mem;

// A linked list of struct blocks that identify the portions of the memory region that are free (not in use). Blocks in this list are stored in increasing address order.
struct block *freelist;

// A linked list of struct blocks that identify portions of memory that have been reserved by calls to smalloc. When a block is allocated it is placed at the front of this list, so the list is unordered.
struct block *allocated_list;

//Allocates a block of memory starting at list and ending at position:
void insert_block(struct block *list, int position) {
    
    //allocated_list
    if (allocated_list == NULL) {
        allocated_list = malloc(sizeof(struct block));
        allocated_list->addr = list->addr;
        allocated_list->size = position;
        allocated_list->next = NULL;
    }
    else {
        struct block *new_block = malloc(sizeof(struct block)); //check!
        //allocated_list is always the most recent item in list (bec we are prepending!)
        new_block->addr = allocated_list->addr + position;
        new_block->size = position;
        new_block->next = allocated_list;
        allocated_list = new_block;
    }
    
    //freelist
    list->addr += position;
    list->size -= position;
}

void remove_block(struct block **list, int position) {
}

void *smalloc(unsigned int nbytes) {
    //TODO
    if (nbytes % 8 != 0) {
        // resize nbytes so it divides 8:
        nbytes = nbytes - (nbytes % 8) + 8;
    }
    struct block *curr = freelist;
    while (curr != NULL) {
        if (curr->size >= nbytes) {
            insert_block(curr, nbytes);
            break;
        }
        curr = curr->next;
    }
    return NULL;
}

int sfree(void *addr) {
    //TODO
    return -1;
}


/* Initialize the memory space used by smalloc,
 * freelist, and allocated_list
 * Note:  mmap is a system call that has a wide variety of uses.  In our
 * case we are using it to allocate a large region of memory.
 * - mmap returns a pointer to the allocated memory
 * Arguments:
 * - NULL: a suggestion for where to place the memory. We will let the
 *         system decide where to place the memory.
 * - PROT_READ | PROT_WRITE: we will use the memory for both reading
 *         and writing.
 * - MAP_PRIVATE | MAP_ANON: the memory is just for this process, and
 *         is not associated with a file.
 * - -1: because this memory is not associated with a file, the file
 *         descriptor argument is set to -1
 * - 0: only used if the address space is associated with a file.
 */
void mem_init(int size) {
    mem = mmap(NULL, size,  PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    //mmap returns a pointer to a block of memory (i.e., a big array of bytes) where our file contents are stored.
    // Our objective: Initialize the memory space used by smalloc, freelist, and allocated_list.
    // Note: mmap is a system call that has a wide variety of uses. In our case we are using it to allocate a large region of memory.
    if(mem == MAP_FAILED) {
         perror("mmap");
         exit(1);
    }
    freelist = malloc(sizeof(struct block));
    // Don't forget 2 free memory from malloc call.
    freelist->addr = mem;
    freelist->size = size;
    freelist->next = NULL;
    allocated_list = NULL;
}

void mem_clean(){
    //TODO
}


//main function for Testing Only. Remove B4 Submission or running make
int main(void) {
    
    
    mem_init(4096*64);
    
    char *ptrs[10];
    int i;

    /* Call smalloc 4 times */
    
    for(i = 0; i < 4; i++) {
        int num_bytes = (i+1) * 10;
    
        ptrs[i] = smalloc(num_bytes);
    }
    printf("%s", *ptrs);
    mem_clean();
    return 0;
}

