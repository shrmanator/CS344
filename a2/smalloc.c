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


void *smalloc(unsigned int nbytes) {
	//TODO
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
    // 1. size: the size of the block that we want to allocate.
    mem = mmap(NULL, size,  PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    // 2. PROT_READ | PROT_WRITE: we will use the allocated block for both reading and writing.
    // 3. MAP_PRIVATE | MAP_ANON: the memory is just for this process, and is not associated with a file.
    // 4. -1: the allocated memory is not associated with a file, so we set it to -1.
    // 5. 0: The space we allocated is not assocciated with any file, so we'll set this to 0.
    // 6. mmap returns a pointer to a block of memory (i.e., a big array of bytes) where our file contents are stored.
    
    // Our objective: Initialize the memory space used by smalloc, freelist, and allocated_list.
    // Note: mmap is a system call that has a wide variety of uses. In our case we are using it to allocate a large region of memory.
    
    if(mem == MAP_FAILED) {
         perror("mmap");
         exit(1);
    }
    // 1. Create a struct block node. The starting address is the one returned by mmap.
}

void mem_clean(){

	//TODO
}

