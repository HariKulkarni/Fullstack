#include<stdio.h>
int main()
{
	int i,j,k,n=01,key;
	printf("enter the no of rows: \n");
	scanf("%d",&key);
	for(i=01;i<=key;i++)
	{
		for(k=key;k>=i;k--)
		{
			printf(" " );
		}
		for(j=1;j<=i;j++)
		{
			printf("%d ",n);
			n++;
		}
		printf("\n");
	}
	
}
