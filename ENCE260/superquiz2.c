#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>  
#include <stdbool.h>
#include <math.h>

// Common declarations
#define MAX_TEXTFILE_SIZE 4096
#define MAX_FILENAME_LENGTH 80
#define MAX_NUMBER_AGENTS         15
#define MAX_AGENTNAME_LENGTH      45
#define MAX_LINE_LENGTH           96


typedef struct {
    char name[MAX_AGENTNAME_LENGTH];
    size_t key;
} Agent;


typedef struct {
    size_t size;
    size_t next;
    Agent pool[MAX_NUMBER_AGENTS];
} AgentPool;

size_t readText(FILE* file, char text[], size_t maxTextSize);
size_t readCipherBook(FILE* file, char text[], size_t maxTextSize);
size_t readMessage(FILE* file, char text[], size_t maxTextSize);

void initAgentPool(AgentPool* agentPool);
Agent* newAgent(AgentPool* agentPool);
void deleteAgent(Agent* agent, AgentPool* agentPool);
Agent* readAgent(FILE* file, AgentPool* agentPool);
Agent* findAgent(char name[], AgentPool* agentPool);
void readAgentName(char agentName[], size_t maxAgentNameLength);
Agent* findAgent(char name[], AgentPool* agentPool);
void encryptMessage(char book[], size_t bookLength, Agent* agent, char message[], size_t messageLength);
void decryptMessage(char book[], size_t bookLength, Agent* agent, char message[], size_t messageLength);


size_t readText(FILE* file, char text[], size_t maxTextSize)
{
    char line[maxTextSize];
    int count = 0;
    while (fgets(line, maxTextSize, file) && count < maxTextSize-1) {
        int i = 0;
        for (i = 0; i < strlen(line) && line[i] != '\0' && count < maxTextSize-1; i++) {
            text[count] = line[i];
            count++;
        }
    }
    return strlen(text);
}


size_t readCipherBook(FILE* file, char text[], size_t maxTextSize)
{
    int len = readText(file, text, maxTextSize);
    int count = 0;
    char *copy = text;
    if (isspace(*copy)) {
        ++copy;
        count++;
    }
    while ((*text++ = *copy++)) {
        while (isspace(*copy)) {
            ++copy;
            count++;
        }
    }
    text = copy;
    return len - count;
}


size_t readMessage(FILE* file, char text[], size_t maxTextSize)
{
    int len = readText(file, text, maxTextSize-1);
    int i;
    int pos = 0;
    for (i = 0; i < len; i++) {
        if (text[i] >= ' ' && text[i] <= '~') {
            text[pos] -= 31;
            pos++;
        } else if (text[i] == '\t') {
            text[pos] = 96;
            pos++;
        } else if (text[i] == '\n') {
            text[pos] = 97;
            pos++;
        }
    }
    return pos;
}


// A function to initialise an AgentPool structure
void initAgentPool(AgentPool* agentPool)
{
    agentPool->size = MAX_NUMBER_AGENTS;
    agentPool->next = 0;
}


// A function to read a file with agent data in it, adding the agent to a agentlist and returning a reference to the agent
Agent* readAgent(FILE* file, AgentPool* agentPool)
{
    char line[MAX_LINE_LENGTH];
    int successAgentName = 0; 
    int successAgentKey = 0;
    Agent* agent = newAgent(agentPool);

    if (fgets(line, MAX_LINE_LENGTH, file) && agent) {
        size_t i;
        for (i = 0; i < strlen(line) && line[i] != ',' && i < MAX_AGENTNAME_LENGTH-1; i++) {
            agent->name[i] = line[i];
        }
        agent->name[i] = '\0';
        while (i < strlen(line) && line[i] != ',') {
            i++;
        }
        if (line[i] == ',' && strlen(agent->name) > 0) {
            i++;
            successAgentName = 1;
            successAgentKey = sscanf(line+i, "%zu", &agent->key) == 1;
        }
    }
    if (agent && !(successAgentName && successAgentKey)) {
        deleteAgent(agent, agentPool);
        agent = NULL;
    }
    return agent;
}


// A function to delete an agent from an AgentPool
void deleteAgent(Agent* agent, AgentPool* agentPool)
{
    int i;
    int move = 0;
    for (i = 0; i < agentPool->next-1; i++) {
        if (move || &agentPool->pool[i] == agent) {
            move = 1;
            agentPool->pool[i] = agentPool->pool[i+1];
        }
    }

    agentPool->next--;
}


void readAgentName(char agentName[], size_t maxAgentNameLength)
{
    char c;
    size_t i;

    c = getchar();
    for (i = 0; i < maxAgentNameLength-1 && c != '\n'; i++) {
        agentName[i] = c;
        c = getchar();
    }
    agentName[i] = '\0';
}


Agent* newAgent(AgentPool* agentPool)
{
    Agent* agent = NULL;
    if (agentPool->next < agentPool->size) {
        agent = &agentPool->pool[agentPool->next];
        agentPool->next++;
    }
    return agent;
}


Agent* findAgent(char name[], AgentPool* agentPool)
{
    Agent* agent = NULL;
    Agent* test = NULL;
    int i = 0;
    int done = 0;
    while (i < agentPool->size && done == 0) {
        test = &agentPool->pool[i];
        if (strncmp(name, test->name, MAX_AGENTNAME_LENGTH)==0) {
            agent = test;
            done = 1;
        }
        i++;
    }
    return agent;
}
    
    
void encryptMessage(char book[], size_t bookLength, Agent* agent, char message[], size_t messageLength)
{
    int booki = agent->key;
    int messi = 0;
    while (messi < messageLength) {
        message[messi] = (message[messi] + book[booki % bookLength]) % 98;
        messi++;
        booki++;
    }
}


void decryptMessage(char book[], size_t bookLength, Agent* agent, char message[], size_t messageLength)
{
    int booki = agent->key;
    int messi = 0;
    while (messi < messageLength) {
        message[messi] = ((message[messi] - book[booki % bookLength]) + (98 * 5)) % 98;
        messi++;
        booki++;
    }
    printf("\n\n%s\n\n", message);
}



int main(void)
{
    char filename[80] = "";
    char agentname[MAX_AGENTNAME_LENGTH] = "";
    FILE* file = NULL;
    char book[MAX_TEXTFILE_SIZE] = "";
    char message[MAX_TEXTFILE_SIZE] = "";
    size_t bookLength = 0;
    size_t messageLength = 0;
    AgentPool agentPool;
    Agent* agent = NULL;
    
    // Read in the cipher book
    scanf("%80s", filename);
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found... program will fail with segmentation fault\n");
    }
    bookLength = readCipherBook(file, book, MAX_TEXTFILE_SIZE);
    fclose(file);
    
    // Read in the message
    scanf("%80s", filename);
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found... program will fail with segmentation fault\n");
    }
    messageLength = readMessage(file, message, MAX_TEXTFILE_SIZE);
    fclose(file);
    
    scanf("%80s", filename);
    initAgentPool(&agentPool);
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("File not found... program will fail with segmentation fault\n");
    }
    while (!feof(file)) {
        readAgent(file, &agentPool);
    }
    fclose(file);
    
    getchar();
    readAgentName(agentname, MAX_AGENTNAME_LENGTH);
    agent = findAgent(agentname, &agentPool);
    if (agent != NULL) {
        encryptMessage(book, bookLength, agent, message, messageLength);
        printf("Secret message is: ");
        for(size_t i=0; i < messageLength; i++) {
            printf(" %d", message[i]);
        }
        decryptMessage(book, bookLength, agent, message, messageLength);
        printf("\nDecrypted message is: %d\n", *message);
    } else {
        printf("No Agent found by the name %s\n", agentname);
    }
    return 0;
}

