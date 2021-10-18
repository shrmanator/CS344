
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>


#define PREFIX "movies_"
#define MAXFILESIZE 500
#define MAXCHARS 500 
#define TRUE 1


struct movie {
        char * title;
        int * year;
        char * language[5][20];
        float * rating;
        struct movie* next;
};


struct movie* createMovie(char* currLine) {
        //1) EXTRACT MOVIE TITLE
        struct movie* currMovie = malloc(sizeof(struct movie));
        char * saveptr = NULL;
        char * languageStr = NULL;
        char* ratingstr = NULL;

        char * token = strtok_r(currLine, ",", &saveptr);
        // allocate memory to movie->title and copy in the extracted title (why did i add 2 again?)
        currMovie->title = calloc(strlen(token) + 2, sizeof(char));
        strcpy(currMovie->title, token);

        //2) EXTRACT MOVIE RELEASE DATE
        token = strtok_r(NULL, ",", &saveptr);
        currMovie->year = atoi(token);

        //3) EXTRACT MOVIE LANGUAGE(S) here it extracts right up (not including) the "]"
        // need help here
        token = strtok_r(NULL, "]", &saveptr);

        // copy extraced info into a string:
        languageStr = calloc(strlen(token) + 1, sizeof(char));
        strcpy(languageStr, token);
        // remove the annoying first '[' with memove (at index 0) using memmove:
        memmove(&languageStr[0], &languageStr[1], strlen(languageStr));

        //aaand, now we have to split up everything....
        int currIndex = 0;
        token = strtok(languageStr, ";");
        while (token != NULL) {
                currMovie->language[currIndex][0] = token;
                char* movieLan = currMovie->language[currIndex][0];
                token = strtok(NULL, ";");
                currIndex++;
        }

        token = strtok_r(NULL, "\n", &saveptr);


        //4) FINALLY! EXTRACT MOVIE RAITING:
        ratingstr = calloc(strlen(token) + 1, sizeof(char));
        strcpy(ratingstr, token);
        memmove(&ratingstr[0], &ratingstr[1], strlen(ratingstr));

        currMovie->rating = ratingstr;
        // convert to floatty
        *(currMovie->rating) = atof(currMovie->rating);
        currMovie->next = NULL;
        return currMovie;
}

/* 
Adds all the movies from the input file <fileName>
and returns the head of the linked list containing them.
*/
struct movie* extractMoviesFromFile(char* filePath){
        FILE * movieFile = fopen(filePath, "r");
        
        char * currLine = NULL;
        size_t len = 0;
        ssize_t nread;
        int count = 0;
        
        struct movie* head = NULL;
        struct movie* tail = NULL;
        
        getline(&currLine, &len, movieFile);

        while ((nread = getline(&currLine, &len, movieFile)) != -1){
            count++;

            // create a new movie using the currLine's info:
            struct movie* newNode = createMovie(currLine);

            // now add the movie to our linked list.
            if (head == NULL) {
                head = newNode;
                tail = newNode;
            }
            else {
                tail->next = newNode;
                tail = newNode;  // the local tail now points to newNode 
            }
        }
        free(currLine);
        fclose(movieFile);
        return head;
}

const char* getFilenameExt(const char *filename) {
    const char *dot = strrchr(filename, '.');
    if(!dot || dot == filename) return "";
    return dot + 1;
}

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

char* getLargestFileInCurrDir() {
    /*
    Returns a string with the name of the largest CSV file with prefix "movies_".
    in the current directory and process it.

    filePrefix : prefix of filename (eg., "movies_")
    sortingType: "smallest" or "largest"
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
    char* fileName = malloc(MAXCHARS);

    //2. iterate thru file sizes in curr directory
    off_t currFileSize = 0;
    while( (aDir = readdir(currDir)) != NULL ){
        if( strncmp(PREFIX, aDir->d_name, strlen(PREFIX) ) == 0){
            if ( strcmp("csv", getFilenameExt(aDir->d_name)) == 0 ) {
                // 3. Get rest of meta-data for the current entry
                stat(aDir->d_name, &dirStat);
                if (dirStat.st_size > currFileSize) { 
                    currFileSize = dirStat.st_size;
                    fileName = aDir->d_name;
                }
            }
        }
    }
    //4. close directory
    closedir(currDir);
    return fileName;
}

char* getSmallestFileInCurrDir() {
    /*
    Returns a string with the name of the largest CSV file with prefix "movies_".
    in the current directory and process it.

    filePrefix : prefix of filename (eg., "movies_")
    sortingType: "smallest" or "largest"
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
    char* fileName = malloc(MAXCHARS);

    //2. iterate thru file sizes in curr directory
    off_t currFileSize = 10000000;
    while( (aDir = readdir(currDir)) != NULL ){
        if( strncmp(PREFIX, aDir->d_name, strlen(PREFIX) ) == 0){
            if ( strcmp("csv", getFilenameExt(aDir->d_name)) == 0 ) {
                // 3. Get rest of meta-data for the current entry
                stat(aDir->d_name, &dirStat);
                if (dirStat.st_size < currFileSize) { 
                    currFileSize = dirStat.st_size;
                    fileName = aDir->d_name;
                }
            }
        }
    }
    //4. close directory
    closedir(currDir);
    return fileName;
}


void populateFile(int fileDescriptor, struct movie* movie) {
    /*
    Writes the titles of every movie
    released in that year, one on each line
    to the file
    */

    struct movie* currMovie = movie;
    while (currMovie != NULL) {
        if (currMovie->year == movie->year) {
            // If file doesn't exist:
            if( currMovie->title == movie->title) {

                // we need to first add an "\n" to the movie title:
                char* movieTitle = malloc(strlen(currMovie->title) + 1);
                strcat(movieTitle, currMovie->title);
                strcat(movieTitle, "\n");
    
                // now we can write the line to file:
                write(fileDescriptor, movieTitle, strlen(movieTitle));
            }
        }
        currMovie = currMovie->next;
    }
}

/*
Iterates throught the given linked list of movie structs
and populates the given directory <nameOfDir> with files that
have names based off the movie years.
CURRENT
*/
void populateDirectory(char* nameOfDir, struct movie * movieList) {
    struct movie * currMovie = movieList;

    // NOTE: No point of checking if directory exits, since dir name if random

    struct dirent* aDir;
    printf("%s", nameOfDir);

    // PART 1: Append all correctly formatted files to currDir:
    while (currMovie != NULL) {
        // Create the string <pathFile> containing the path's file name and .txt extension,
        // then add it to the <nameOfDir> directory:
        char pathFile[MAXCHARS];
        sprintf(pathFile, "./%s/%d.txt", nameOfDir, currMovie->year); 
        // Now open the file for reading / writing (reading is really just for testing):
        int fileDescriptor = open(pathFile, O_APPEND | O_RDWR | O_CREAT, 0777); 
        // PART 2: Within the file, we will now write the titles of all the movies
        // released in that year, one on each line (might as well while the file's still open):
        populateFile(fileDescriptor, currMovie);
        
        currMovie = currMovie->next;
    }
}


void processFile(char* fileName) {
    /*
    Does complete "process" for the given file <fileName>
    */

    // 1. Forms the string that represents the name of the directory
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

    // Create the directory and call it <osuid>.<filename>.<number>
    mkdir(nameOfDir, 0750);

    // 2. Look at each movie in <filename> and extracts the year it was released (CURRENT)
    struct movie * processedMovies = extractMoviesFromFile(fileName);
    // 3. Populate the directory:
    populateDirectory(nameOfDir, processedMovies);
    // don't think we'll need this string anymore (contents copied to other string)
    free(stringifyTheInt); 
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
            char* largestFile = getLargestFileInCurrDir();
            printf("Now processing the chosen file named %s\n\n", largestFile);
            //2. get largest .csv file and pass file into processFile.
            processFile(largestFile);
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
            char* smallestFile = getSmallestFileInCurrDir();
            printf("Now processing the chosen file named %s\n\n", smallestFile);
            //2. get largest .csv file and pass file into processFile.
            processFile(smallestFile);
            //3. return back to submenu
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
