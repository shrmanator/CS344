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

void insert_new_block(struct block** list, int position) {
    // link the inserted block and resize.
    
}

void remove_the_block(struct block** list, int position) {
    // unlink the targeted block and resize.
}

/* Searches the freelist for a block that is
 at least nbytes bytes in size. */
void *smalloc(unsigned int nbytes) {
    //TODO
    if (nbytes % 8 != 0) {
        // Make sure 8|nbytes:
        nbytes = nbytes - (nbytes % 8) + 8;
    }
    struct block *curr_block = freelist;
    while (curr_block != NULL) {
        if (curr_block->size == nbytes) {
            insert_new_block();
        }
        curr_block = curr_block->next;
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
    // Code starts here:
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
