#include <stdio.h>
#include <string.h>
    
/* Reads the image from the open file fp into the two-dimensional array arr
 * num_rows and num_cols specify the dimensions of arr
 */
void read_image(int num_rows, int num_cols, int arr[num_rows][num_cols], FILE *fp) {
    // NOT READING FIRST ITEM IN TXT FILE!
    for (int i=0;i<num_rows;i++) {
        for (int j=0; j<num_cols; j++) {
            fscanf(fp, "%d", &arr[i][j]);
        }
    }
}

/* Print to standard output the contents of the array arr */
void print_image(int num_rows, int num_cols, int arr[num_rows][num_cols]) {
    for (int i=0; i<num_rows; i++) {
            for (int j=0; j<num_cols; j++) {
                printf(" %d", arr[i][j]);
            }
    }
}

/* TODO: Write the count_cells function */
void count_cells(int num_rows, int num_cols, int arr[num_rows][num_cols]){
    int single_cell_size = 0;
    int total_cells = 0;
    int visitied = 0;
    
    for (int i=0; i<num_cols; i++) {
        for (int j=0; j<num_rows; j++) {
            if (arr[i][j] == 225) {
                arr[i][j] = -1;
                if (i - 1 < 0) {
                    // the value above
                    if (arr[i - 1][j] != 0) {
                        arr[i-1][j] = -1;
                        visitied = 1;
                        }
                }
                if (i + 1 > num_rows) {
                    // the value below
                    if (arr[i + 1][j] != 0) {
                        arr[i+1][j] = -1;
                        visitied = 1;
                        
                    // the value left
                    // the value right
                    }
                }
            }
        }
    }
}


    
       
