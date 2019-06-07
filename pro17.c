#include <stdio.h>
int main()
{
    int n2,k1,ak1[100],i1,j1,c1=0;
    scanf("%d%d",&n2,&k1);
    for(i1=0;i1<n2;i1++)
    {
    	scanf("%d",&ak1[i1]);
    }
    for(i1=0;i1<n2;i1++)
    {  
    	for(j1=i1+1;j1<n2;1++)
    	{
    		if(ak1[i1]+ak1[j1]==k1)
    		{
    			c1++;
    		}
    	}
   	}
    if(c1>=1)
    {
    	printf("yes");
    }
    else
    {
    	printf("no");
    }
	return 0; 
}
