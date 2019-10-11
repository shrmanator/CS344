#include <stdio.h>
#include <string.h>
#include <ctype.h>
    
/* Reads the image from the open file fp into the two-dimensional array arr
 * num_rows and num_cols specify the dimensions of arr
 */
void read_image(int num_rows, int num_cols, int arr[num_rows][num_cols], FILE *fp) {
    // NOT READING FIRST ITEM IN TXT FILE!
    for (int i=0;i<num_rows;i++) {
        for (int j=0; j<num_cols; j++) {
            int num = 0;
            fscanf(fp, "%d", &num);
                arr[i][j] = num;
        }
    }
}

/* Print to standard output the contents of the array arr */
void print_image(int num_rows, int num_cols, int arr[num_rows][num_cols]) {
    for (int i=0; i<num_rows; i++) {
            for (int j=0; j<num_cols; j++) {
                printf(" %d", arr[i][j]);
        
            }
            printf("\n");
    }
}

/* TODO: Write the count_cells function */
void count_cells(int num_rows, int num_cols, int arr[num_rows][num_cols]){
    int total_cells = 0;
    int visited = 0;
    for (int i=0; i<num_rows; i++) {
        for (int j=0; j<num_cols; j++) {
            if (arr[i][j] == -1) {
                if (i - 1 >= 0) {
                    if (i + 1 < num_rows) {
                        if (j - 1 > 0) {
                            if (j + 1 < num_cols) {
                                arr[i][j] = -1;
                                visited--;
                            }
                        }
                    }
                }
            }
            if (arr[i][j] == 255) {
                arr[i][j] = -1;
                // the value above
                if (i - 1 >= 0) {
                    if (arr[i - 1][j] == 255) {
                        arr[i - 1][j] = -1;
                        visited++;
                        }
                }
                // the value below
                if (i + 1 < num_rows) {
                    if (arr[i + 1][j] == 255) {
                        arr[i + 1][j] = -1;
                        visited++;
                    }
                }
                // the value left
                if (j - 1 > 0) {
                    if (arr[i][j - 1] == 255) {
                        arr[i][j - 1] = -1;
                        visited++;
                    }
                }
                // the value right
                if (j + 1 < num_cols) {
                    if (arr[i][j + 1] == 255 ) {
                        arr[i][j + 1] = -1;
                        visited++;
                    }
                }
            }
        }
    }
    printf("Number of Cells is %d\n", visited);
}
