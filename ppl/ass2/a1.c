#include <stdio.h>

int main() {
	int a[5];
	for(int i=0;i<100000000000;i++) {
		a[i] = 'a';
		printf("%d %d\n", a[i], i);
	}
	return 0;
}
