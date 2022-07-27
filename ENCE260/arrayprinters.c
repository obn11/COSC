// Program to demonstrate use of pointers to manipulate arrays

#include <stdio.h>

// A simple Java-like version using array indexing
void arrayPrinter1(const int a[], int n)
{
    printf("arrayPrinter1:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("First array element: %d\n\n", a[0]);
}

// A version using pointer arithmetic instead of indexing
void arrayPrinter2(const int* a, int n)
{
    printf("arrayPrinter2:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", *(a + i));
    }
    printf("First array element: %d\n\n", a[0]);
}

// A version using autoincrement on a pointer
void arrayPrinter3(const int* a, int n)
{
    printf("arrayPrinter3:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", *a++);
    }
    printf("First array element: %d\n\n", a[0]);
}

// A version that dispenses with a loop control variable
void arrayPrinter4(const int* a, int n)
{
    const int* endOfArray = a + n;
    printf("arrayPrinter4:\n");
    while (a < endOfArray) {
        printf("%d ", *a++);
    }
    printf("First array element: %d\n\n", a[0]);
}

char data[100];
int isInData(char* address)
{
    return ((address >= data) && (address <= (data + 99)));
}

int isInData2(char data[], int arraySize, char* ptr) 
{
    return ((ptr >= data) && (ptr <= (data + arraySize -1)));
}

int myIndex(int data[], int* element)
{
    return element - data;
}


int main(void)
{
    int data[30];
    int* p = &data[17];
    printf("Index is %d\n", myIndex(data, p));
}


