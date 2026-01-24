#include<stdio.h>
int main(){
	int i,j,num;
	for(i=1;i<=9;i++){
		num=1;
		for(j=1;j<=i;j++){
			if(j %2==1){
				printf(" * ");
			}
			else{
				printf("%d",num);
				num+=2;
			}
		}
		printf("\n");
	}
	printf(" T E C H W A R 2026\n");
	for(i=11;i>=3;i--){
		for(j=3;j<=i;j++){
			printf (" %d",j);
		}
		printf ("\n");
	}
}
