#include <stdio.h>
#include <stdlib.h>

int main (void)
{
	unsigned int *ptr = (unsigned int*)malloc(10000*sizeof(int));
	*ptr = -1;
	printf("%p\tshort:%i\tint:%i\tlong:%i\n ",ptr,(int)sizeof(short),(int)sizeof(int),(int)sizeof(long));
	printf("%u\n",*ptr);
	free(ptr);
	return 0;
}
	
