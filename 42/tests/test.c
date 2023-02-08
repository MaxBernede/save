#include <stdio.h>
#include <stdlib.h>


int main()
{
	float y1;
	float x1;
	float y2;
	float x2;
	int o;

	x1 = 0.0;
	x2 = 10.0;
	y1 = 0.0;
	y2 = 50.0;

	o = (y2 - y1)/(x2 - x1);
	printf("I de %d\n", o);
	return 0;
}

