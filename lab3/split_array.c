#include <stdio.h>
#include <stdlib.h>

/* Return a pointer to an array of two dynamically allocated arrays of ints.
   The first array contains the elements of the input array s that are
   at even indices.  The second array contains the elements of the input
   array s that are at odd indices.

   Do not allocate any more memory than necessary.
*/
int **split_array(const int *full_array, int argc) {
    int **deep_array = (int**) malloc(2 * sizeof(int*));
    
    int even = 0;
    int odd = 0;

    for(int i=0;i<argc;i++){
        if(full_array[i]%2 == 0) {
            even++;
        } else {
            odd++;
        }
    }
    deep_array[0] = malloc(sizeof(int) * even);
    deep_array[1] = malloc(sizeof(int) * odd);
    
    int k = 0;
    int m = 0;
    for(int j=0;j<argc;j++){
        if(full_array[j]%2 == 0) {
            deep_array[0][k] = full_array[j];
            k++;
        } else {
            deep_array[1][m] = full_array[j];
            m++;
        }
    }
    return deep_array;
}

/* Return a pointer to an array of ints with size elements.
   - strs is an array of strings where each element is the string
     representation of an integer.
   - size is the size of the array
 */

int *build_array(char **strs, int size) {
    int *array = (int*) malloc(size - 1 * sizeof(int));
    for(int i=0;i<size-1;i++){
        array[i] = *strs[i+1] - '0';
    }
    return array;
}


int main(int argc, char **argv) {
    /* Replace the comments in the next two lines with the appropriate
       arguments.  Do not add any additional lines of code to the main
       function or make other changes.
     */
    int *full_array = build_array(argv, argc);
    int **result = split_array(full_array, argc);

    printf("Original array:\n");
    for (int i = 0; i < argc - 1; i++) {
        printf("%d ", full_array[i]);
    }
    printf("\n");

    printf("result[0]:\n");
    for (int i = 0; i < argc/2; i++) {
        printf("%d ", result[0][i]);
    }
    printf("\n");

    printf("result[1]:\n");
    for (int i = 0; i < (argc - 1)/2; i++) {
        printf("%d ", result[1][i]);
    }
    printf("\n");
    free(full_array);
    free(result[0]);
    free(result[1]);
    free(result);
    return 0;
}
