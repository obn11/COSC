/*********************************************
 * celsius.c (King Chapter 2, page 2)
 * Cnverts a Fahrenheit temperature to Celsius
 * Slightly Modified by RJL
 * *******************************************/
#include <stdio.h>

#include <stdlib.h>

#define FREEZING_PT 32.0
#define SCALE_FACTOR (5.0 / 9.0)

int main(void)
{
	float fahrenheit = 0;
	float celsius = 0;
	printf("Enter Fashrenheit temperature: ");
	
	scanf("%f", &fahrenheit);
	celsius = (fahrenheit - FREEZING_PT) * SCALE_FACTOR;
	
	printf("Celsius equivalent: %.lf\n", celsius);
	return EXIT_SUCCESS;
}
