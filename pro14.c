#include <stdio.h>
int main()
{
	int n2,q,p[10],r[10],a[10],i1,j,s;
	scanf("%d %d",&n2,&q);
	for(i1=1;i1<=n2;i1++)
	{
	    scanf("%d",&a[i1]);
	}
	for(s=1;s<=q;s++)
	{
	    scanf("%d %d",&p[s],&r[s]);
	}
		for(s=1;s<=q;s++)
	{
	     int x=0;
	    for(i1=p[s];i1<=r[s];i1++)
	    {
	      x=x^a[i1];
	      
	    }
	   printf("%d\n",x);
	}

	    return 0;
}
