#include <stdio.h>
#include <stdlib.h>

#define SCALE_FACTOR 1.609344

int main(void)
{
	float mile = 0;
	float kilometre = 0;
	printf("How many miles? ");
	
	scanf("%f", &mile);
	kilometre = mile * SCALE_FACTOR;
	
	printf("That's %.2f km.\n", kilometre);
	return EXIT_SUCCESS;
}
