#include <stdio.h>

#define MAX_INPUT_MESSAGE_LENGTH 4096
#define MAX_KEY_LENGTH 1024
#define MAX_TEXT_LENGTH 3072




// A function to read a small format (8-bit) number
int readUCharInt(unsigned char* input)
{ 
    int size;
    size = scanf("%hhu", input);
    return size;
}


int readInput(unsigned char input[], size_t inputMaxLength)
{
    unsigned char x = 0;
    int i = 0;
    int c = 0;
    
    while ((c = readUCharInt(&x)) != -1 && i < inputMaxLength) {
        input[i++] = x;                                                                                                                                                
    }
    if (i > inputMaxLength-1) {
        i = -1;
    } 
    return i;
}

int splitInput(unsigned char input[], size_t inputLength, int section, unsigned char part[], size_t maxPartLength)
{
    int i = 0;
    int marker = 0;
    int q = 0;
    
    marker = input[0];
    i += 1;
    while (input[i] != marker) {
        if ((section == 0) && (i < maxPartLength)) {
            part[q++] = input[i];
        }
        i += 1;
    }
    i += 1;
    if (section == 1) {
        while ((i < maxPartLength) && (i < inputLength)) {
            part[q++] = input[i];
            i += 1;
        }
    }
    if (i > maxPartLength - 1) {
        q = -1;
    }
    return q;
}

void decryptMessage(unsigned char key[], size_t keyLength, unsigned char message[], size_t messageLength)
{
    int i = 0;
    int keyn = 0;
    
    while (i < messageLength) {
        if (keyn == keyLength) {
            keyn = 0;
        }
        message[i] = message[i] - key[keyn];
        i += 1;
        keyn += 1;
    }
    message[i+1] = 0;
}

int main()

{
    unsigned char input[MAX_INPUT_MESSAGE_LENGTH];
    unsigned char key[MAX_KEY_LENGTH];
    unsigned char message[MAX_TEXT_LENGTH];
    
    int inputLength = readInput(input, MAX_INPUT_MESSAGE_LENGTH);
    int keyLength = splitInput(input, inputLength, 0,key, MAX_KEY_LENGTH);
    int messageLength = splitInput(input, inputLength, 1,message, MAX_TEXT_LENGTH);
    
    decryptMessage(key, keyLength, message, messageLength);
    for(int i=0; i < messageLength+1; i++) printf("%c", message[i]);
    printf("\n");
}


int nain()
{
    unsigned char input = 0;
    int result = 0;
    
    result = readUCharInt(&input);
    if (result == EOF) {
        printf("No input\n");
    } else if ((input >= 32) && (input <= 127)) {
        printf("Read number %i with ASCII symbol %c\n", input, input);
    } else {
        printf("Read number %i - non-printable character\n", input);
    }
    return 0;
}
