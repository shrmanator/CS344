
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>

#define PREFIX "movies_"
#define MAXFILESIZE 255
#define MAXCHARS 255
#define TRUE 1


char* removeFileExtension(char* myStr) {
    char *retStr;
    char *lastExt;
    if (myStr == NULL) 
        return NULL;
    if ((retStr = malloc (strlen (myStr) + 1)) == NULL) 
        return NULL;
    strcpy (retStr, myStr);
    lastExt = strrchr (retStr, '.');
    if (lastExt != NULL)
        *lastExt = '\0';
    strcat(retStr, ".");
    return retStr;
}


int fileExists(char* fileName) {
    /*
    returns whether input file exits.
    */

}

//CURRENT
void processFile(char* fileName) {
    /*
    Process the given file fileName
    */

    // 1. remove the .csv extension from fileName:
    char* trimmedFileName = removeFileExtension(fileName);

    const char* OSUID = "sherma73.";
    int randomInt = rand() % 100000;  // int range is 0 to 99999

    char * nameOfDir = malloc(strlen(trimmedFileName) + strlen(OSUID) + sizeof(randomInt) + 1);

    // OSUID = sherma73. (my student name)
    strcat(nameOfDir, OSUID);
    // adding the filename to the directory name
    strcat(nameOfDir, trimmedFileName);

    char * stringifyTheInt = malloc(50);
    sprintf (stringifyTheInt, "%d", randomInt);
    strcat(nameOfDir, stringifyTheInt);
}

char* getLargestFileInCurrDir(char* filePrefix) {
    /*
    Returns a string with the name of the largest CSV file with prefix "movies_".
    in the current directory and process it.

    filePrefix : prefix of filename (eg., "movies_")
    */

    // 1. Open current directory:
    DIR* currDir = opendir(".");

    struct dirent * aDir;
    /*
    struct dirent {
        ino_t          d_ino;           ## Inode number
        char           d_name[256];     ## Null-terminated filename 
    */
    
    struct stat dirStat;
    int i = 0;
    off_t fileSize;
    char * fileName = malloc(255);

    //2. iterate thru file sizes in curr directory
    off_t currFileSize = 0;
    while( (aDir = readdir(currDir)) != NULL ){
        if( strncmp(PREFIX, aDir->d_name, strlen(PREFIX) ) == 0){
            // Get meta-data for the current entry
            stat(aDir->d_name, &dirStat);
            if (dirStat.st_size > currFileSize) { 
                currFileSize = dirStat.st_size;
                fileName = aDir->d_name;
            }
        }
    }
    //3. close directory
    closedir(currDir);
    return fileName;
}


char* getSmallestFileInCurrDir() {
    /*
    Returns the smallest file with the extension .csv
    in the current directory whose name starts with the prefix movies_
    and automatically process it.
    */


}


void selectFileToProcess() {
    int userMenuInput;
    char *userFileNameInput = malloc(MAXFILESIZE);
    while (TRUE) {


        // DISPLAY USER MENU
        printf("\n");
        printf("Which file do you want to process?\n");
        printf("Enter 1 to pick the largest file\n");
        printf("Enter 2 to pick the smallest file\n");
        printf("Enter 3 to specify the name of a file\n");
        printf("Enter a choice from 1 to 3: ");
        scanf("%d", &userMenuInput);
        printf("\n");

        // 1. FINDS LARGEST FILE WITH CSV EXTENSION (CURRENT STEP)
        if (userMenuInput == 1) {
            /*
            The program finds the largest file with the extension csv
            in the current directory whose name starts with the prefix movies_
            and automatically process it.

            In case of tie, pick any of the files with the extension
            csv starting with movies_ that have the largest size.
            */

            //1. find largest .CSV file with the prefix movies_
            char* nameOflargestFile = getLargestFileInCurrDir("movies_");
            printf("Now processing the chosen file named %s", nameOflargestFile);
            //2. get largest .csv file and pass file into processFile.
            processFile(nameOflargestFile);
            //3. return back to submenu
            return;
        }

        // 2. FINDS SMALLEST FILE WITH CSV EXTENSION
        if (userMenuInput == 2) {
            /*
            The program finds the smallest file with the extension csv
            in the current directory whose name starts with the prefix movies_
            and automatically process it. 
            
            In case of tie, pick any of the files with the extension csv starting
            with movies_ that have the smallest size.
            */
            // smallestFile = getSmallestFile();
            // printf("Now processing the chosen file named %s", nameOfSmallestFile);
            // processFile(getSmallestFileInDir)
            return;
        }

        // 3.
        if (userMenuInput == 3) {
            //1. The program asks the user to enter the name of a file.
            //   There is no requirement that the file name must start with a
            //   particular prefix or that it must have a particular extension.
            printf("\n");
            printf("Enter the complete file name: ");
            scanf("%s", userFileNameInput);

            // 2. Checks if the userfileNameInput file exists in the current directory.
            if (fileExists(userFileNameInput) == 1) {

                // processFile(); ?? Is this supposed to return anything?

                return;
            }
            // 3. If the file is not found, the program should write an error message and
            // again give the user the 3 choices about picking a file, i.e., don't go back
            // to the main menu, but stay at the menu for picking a file.
            else {
                printf("\n");
                // printf("The file %s was not found. Try again\n", userFileNameInput);
            }
        }

        // If the file is found and has been successfully picked based on any of the 3
        // options picked by the user, the program must print the name of the file that will
        // now be processed.
    }
}


int main() {
    int userInput;

    while (TRUE) {
        printf("\n");
        printf("1. Select file to process\n");
        printf("2. Exit the program\n");
        printf("Enter a choice 1 or 2 (make sure input is an integer): ");
        scanf("%d", &userInput);

        // Select a "movies_" file to process
        if (userInput == 1) {
            selectFileToProcess();
            continue;
        }

        // Exit the program
        else if (userInput == 2) {
            return 0;
        }

        // if invalid user input (repeat menu options)
        else {
            printf("Input '%d' invalid. Enter values 1 or 2", userInput);
            continue;
        }
    }
}
