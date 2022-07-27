/* Program to introduce the 'char' data type, plus the use of getchar and
 * putchar to read and write chars from/to standard input.
 * Reads characters from stdin, printing each one out in both decimal and octal,
 * until '\n' or end-of-file is reached.
 * Written for ENCE260 by RJL.
 * June 2016
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int nain(void)
{
    char someChar = 0;          // A character
    int c = 0;                  // An int with a char in its low byte

    someChar = '*';
    printf("someChar = %c\n", someChar); // Print a single char

    printf("Enter a line of text, terminated by 'Enter'\n");

    // Read and print characters until newline or End-Of-File
    c = getchar();              // Get char (cast to int) or EOF
    while (c != '\n' && c != EOF) {
        printf("Character '%c', decimal %d, octal %o, hexadecimal %x\n", c, c, c, c);
        c = getchar();
    }

    return EXIT_SUCCESS;
}
int lain(void)
{
    int c = 0;
    int temp = 0;
    
    while((c = getchar()) != EOF) {
        if (c == 10) {
            printf("'\\n'\n");
        } else {
            if (isdigit(c)) {
                printf("'%c': Digit %c\n", c, c);
            } else if (isalpha(c)) {
                if (c < 97) {
                    temp = c - 64;
                } else {
                    temp = c - 96;
                } printf("'%c': Letter %d\n", c, temp);
            } else {
                printf("'%c': Non-alphanumeric\n", c);
            }
        }
    }
    return EXIT_SUCCESS;
}

int nmain(void)
{
    int c = 0;
    int counts[26] = {0};
    int i = 'A';
    int x;
    
    while((c = getchar()) != EOF) {
        if (isalpha(c)) {
            c = toupper(c);
            c = c - 'A';
            counts[c] += 1;
        }
    } for (x = 0; x < 26; ++x) {
        printf("%c: %i\n", i, counts[x]);
        i += 1;
    }
    return 0;
}

double discriminant(double a, double b, double c)
{
    double out = 0;
    out = (b*b) - (4 * a * c);
    
    return out;
}

int mmain(void)
{
    printf("%.2lf\n", discriminant(1.5, 1.5, 1.5));
    return 0;
}

/* A program to demonstrate the (mis)use of external
 * variables. Reads a name (well, any string of chars,
 * really), converts it to upper case, then prints it
 * out.
 * Written for ENCE260, June 2011/2015/2018
 * Author: Richard Lobb
 */
 

#define MAX_NAME_LENGTH  80
char name[MAX_NAME_LENGTH];  // declares a global (aka "external") variable

// Read a name (or any string) into the "name" array.
// Terminate it with null.
void readName(void)
{
    int c = 0;
    int i = 0;
    printf("Enter your name: ");
    while ((c = getchar()) != '\n' && c != EOF && i < MAX_NAME_LENGTH - 1) {
        name[i++] = c;
    }
}

// Convert the global "name" string to upper case
void convertNameToUpper(void)
{
    int i = 0;
    while (name[i] != '\0') {
        name[i] = toupper(name[i]);
        i++;
    }
}

// Main program reads name, converts it to upper case and prints it
int main(void)
{
    readName();
    convertNameToUpper();
    printf("Your name in upper case: %s\n", name);
}
    

