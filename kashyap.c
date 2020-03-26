#include <math.h> 
#include <stdio.h> 
#include <conio.h>

// global var -> n //
int n;
int a[10];
int t;

void countDivisors(int n) {
	int count = 0; 
	for (int i = 1; i <= sqrt(n) + 1; i++) 
	{ 
		if (n % i == 0){
			count += (n / i == i) ? 1 : 2; 
        }
	} 
    if(count != 0){
        if (count % 2 != 0){
            //printf("%d",n);
            for(int i=0;i<t;++i){
                scanf("%d",&a[i]);
            }
            for(int i=0;i<t;++i){
                printf("%d\t",a[i]);
            }
        }
    }
}  
int main() { 
    int T; //for the major testcases
    scanf("%d",&T);
    while(T-->0){
        scanf("%d",&t);
        while(t-->0){
            scanf("%d",&n);
            countDivisors(n); 
        }
    }
getch();
return 0;
} 
