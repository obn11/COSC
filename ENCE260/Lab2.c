#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int quad(void)
{
	float a = 0;
	float b = 0;
	float c = 0;
	float dis = 0;
	scanf("%f", &a);
	scanf("%f", &b);
	scanf("%f", &c);
	dis = ((b * b) - (4 * a * c)) < 0;
	if (a == 0) {
		printf("Not a quadratic");
	} else if (dis < 0) {
		printf("Complex roots");
	} else {
		float root1 = 0;
		float root2 = 0;
		root1 = ((-1 * b) + sqrt(dis)) / (2 * a);
		root2 = ((-1 * b) - sqrt(dis)) / (2 * a);
		if (root1 < root2) {
			printf("Roots are %.4f and %.4f\n", root1, root2);
		} else {
			printf("Roots are %.4f and %.4f\n", root2, root1);
		}
	}
}

int main(void)
{
	int num = 0;
	while (num != 42) {
		scanf("%d", &num);
		printf("%d\n", num);
	}
	return 0;
}
