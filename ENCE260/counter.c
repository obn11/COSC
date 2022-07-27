#include <stdio.h>
#include <math.h>


void main()
{
    int i = 0;
    while (i < 1000000000) {
        i++;
    }
    printf("1,000,000\n");
    while (i < 10000000000) {
        i++;
    }
    printf("10,000,000\n");
    while (i < 100000000000) {
        i++;
    }
    printf("100,000,000\n");
    while (i < 1000000000000) {
        i++;
    }
    printf("1,000,000,000\n");
}
