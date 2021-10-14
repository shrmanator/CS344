
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>



//returns whether input file exits.
int fileExists(char* file) {

}


// returns 
char* processFile() {

}


char* getLargestFile() {

}


char* getSmallestFile() {

}


void selectFileToProcess() {
    while (1) {
        int userMenuInput;
        char userFileNameInput[255];

        // DISPLAY USER MENU
        printf("\n");
        printf("Which file you want to process?\n");
        printf("Enter 1 to pick the largest file\n");
        printf("Enter 2 to pick the smallest file\n");
        printf("Enter 3 to specify the name of a file\n");
        printf("Enter a choice from 1 to 3: ");

        scanf("%d", &userMenuInput);

        // FINDS LARGEST FILE WITH CSV EXTENSION (CURRENT STEP)
        if (userMenuInput == 1) {
            /*
            The program finds the largest file with the extension csv
            in the current directory whose name starts with the prefix movies_
            and automatically process it.

            In case of tie, pick any of the files with the extension
            csv starting with movies_ that have the largest size.
            */
            
            //1. find largest file with the prefix movies_
            char nameOfLargestFile[255];
            // getLargestFile(prefix movies_ ???)
            // processFile()
            return;
        }

        // FINDS SMALLEST FILE WITH CSV EXTENSION
        if (userMenuInput == 2) {
            /*
            The program finds the smallest file with the extension csv
            in the current directory whose name starts with the prefix movies_
            and automatically process it. 
            
            In case of tie, pick any of the files with the extension csv starting
            with movies_ that have the smallest size.
            */
            char *nameOfSmallestFile;
            nameOfSmallestFile = getSmallestFile();
            printf("Now processing the chosen file named %s", nameOfSmallestFile);
            return;
        }

        if (userMenuInput == 3) {
            //1. The program asks the user to enter the name of a file.
            //   There is no requirement that the file name must start with a
            //   particular prefix or that it must have a particular extension.
            printf("\n");
            printf("Enter the complete file name: ");
            scanf("%s", userFileNameInput);

            // 2. Checks if the userfileNameInput file exists in the current directory.
            if (fileExists(userFileNameInput) == 1) {
                // process file?
        
                return;
            }
            // 3. If the file is not found, the program should write an error message and
            // again give the user the 3 choices about picking a file, i.e., don't go back
            // to the main menu, but stay at the menu for picking a file.
            else {
                printf("\n");
                printf("The file %s was not found. Try again\n", userFileNameInput);

            }
        }

        // If the file is found and has been successfully picked based on any of the 3
        // options picked by the user, the program must print the name of the file that will
        // now be processed.
    }
}


int main() {
    int userInput;
    printf("\n");
    printf("1. Select file to process\n");
    printf("2. Exit the program\n");
    printf("Enter a choice 1 or 2: ");
    scanf("%d", &userInput);

    // CHOICE 1: SELECT FILE TO PROCESS
    if (userInput == 1) {
        while (userInput == 1) {
            selectFileToProcess();
            // after file processing, bring back up main menu:
            printf("\n");
            printf("1. Select file to process\n");
            printf("2. Exit the program\n");
            printf("Enter a choice 1 or 2: ");
            scanf("%d", &userInput);
        }
    }
    // CHOICE 2: EXIT PROGRAM
    if (userInput == 2) {
        return 0;
    }
}