#include<stdio.h>

int fact(int num) {
	if(n <= 1){
		return 1;
	}
	else {
		return n*fact(n-1);
	}
}


int main() {
	int a = fact(3);
	//printf("%d", fact(3));
	return 0;
}
