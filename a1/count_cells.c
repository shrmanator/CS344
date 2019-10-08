#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LINE_LENGTH 80


void read_image(int num_rows, int num_cols, int arr[num_rows][num_cols], FILE *fp);

void print_image(int num_rows, int num_cols, int arr[num_rows][num_cols]);

void count_cells(int num_rows, int num_cols, int arr[num_rows][num_cols]);

int main(int argc, char **argv) {
    FILE *text;
    char rows_cols_string[LINE_LENGTH + 1]; // This will be converted to an int in num_rows.
    // Open text file for reading:
    text = fopen(argv[1], "r");
    
    //Error checking:
    if (text == NULL || argc < 1 || argc > 3) {
        fprintf(stderr, "Error opening A2.txt\n");
        exit(1);
    }
    if (argv[2] != '\0') {
        if (strcmp(argv[2], "-p") != 0) {
            fprintf(stderr, "Second arg must be -p.\n");
            exit(1);
        }
    }
    
    // Getting num of rows and cols, but it's a string:
    fgets(rows_cols_string, LINE_LENGTH, text);
    // Time to convert to ints:
    char rows_str[LINE_LENGTH];
    char cols_str[LINE_LENGTH];
    int i = 0;
    while(rows_cols_string[i] != ' ') {
        rows_str[i] = rows_cols_string[i];
        i++;
    }
    int j = 0;
    while(rows_cols_string[j] != '\n') {
        cols_str[j] = rows_cols_string[i + 1];
        j++;
        i++;
    }
    //now we convert:
    int rows_int = atoi(rows_str);
    int cols_int = atoi(cols_str);
    
    // Initializing the resulting array to be filled with contents of txt file.
    int text_file_array[rows_int][cols_int];

    read_image(rows_int, cols_int, text_file_array, text);
    if (strcmp(argv[2], "-p") == 0) {
        print_image(rows_int, cols_int, text_file_array);
    }
    count_cells(rows_int, cols_int, text_file_array);

    // Manipulation completed. Close A2.txt:
    if (fclose(text) != 0) {
        fprintf(stderr, "fclose failed\n");
        return 1;
    }
    return 0;
}
