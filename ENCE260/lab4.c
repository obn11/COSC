#include <stdio.h>

void printViaPtr(const int* intPtr)
{
    printf("%d\n", *intPtr);
}

void print2Ints(int a, int b)
{
    
    printViaPtr(&a);
    printViaPtr(&b);
}

void swap(int* address1, int* address2)
{
    int temp = *address1;
    *address1 = *address2;
    *address2 = temp;
}
void oof(char* p1, char* p2)
{
    *p1 = *p2;
}

#include <stdlib.h>
#include <math.h>

void findTwoLargest(const int data[], int n, int* largest, int* secondLargest)
{
    if (data[0] > data[1]) {
        *largest = data[0];
        *secondLargest = data[1];
    } else {
        *largest = data[1];
        *secondLargest = data[0];
    }
    int i = 2;
    while (i < n) {
        if (data[i] > *largest) {
            *secondLargest = *largest;
            *largest = data[i];
        } else if (data[i] > *secondLargest) {
            *secondLargest = data[i];
        }
        i++;
    }
}

// Print the first n elements of array data in braces, comma-separated
void printArray(const int data[], int n)
{
    if (n <= 0) {
        printf("{}");
    }
    else {      
        printf("{%d", data[0]);
        for (int i = 1; i < n; i++) {
            printf(",%d", data[i]);
        }
        printf("}");
    }
}

// Test the function findTwoLargest on array 'data' of length 'n.
// It is assumed that n >= 2.
void test_array(const int data[], int n)
{
    int largest = 0, second = 0;

    findTwoLargest(data, n, &largest, &second);
    printf("The two largest elements from ");
    printArray(data, n);
    printf(" are %d and %d\n", largest, second);
}

// Next, a set of test arrays

int array1[] = { 1, 2, 3, 4, 5, 6 };
int array2[] = { 20, 19, 18 };
int array3[] = { 4, 4, 4, 4 };
int array4[] = { 17, 14 };
int array5[] = { 4, 45, 123, 3, 345, 27, 479 };

// Lastly, the main test routine.
int main()
{
    int data[] = {1, 9, 4, 0, 5, 3};
    int result1 = 0, result2 = 0;
    findTwoLargest(data, 6, &result1, &result2);
    printf("%d %d\n", result1, result2);
}
