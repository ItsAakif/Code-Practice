#include <stdio.h>
void swap(int *a, int *b)
{
 int temp;
 temp = *a;
 *a=*b;
 *b = temp;
 }

void readnum(int a[], int n)
{
  printf("Enter %d elements :",n);
  for(int i=0;i<n;i++)
    scanf("%d",&a[i]);
}
void selsort(int a[], int n)
{
  int ind,large;
  for(int i=0;i<n-1;i++)
   {
   large=a[0];
   ind=0;
   for(int j=1;j<n-i;j++)
    {
     if (a[j]>large)
       {
        large= a[j];
        ind=j;
       }
       
     }
     swap(&a[ind],&a[n-i-1]);
    }
}
void printnum(int a[],int n)
{
  printf("The elements are :\n");
  for(int i=0;i<n;i++)
    printf("%d  \n",a[i]);
}   
void main()
{
int a[100],n;
printf("Enter the length of the array : ");
scanf("%d",&n);
readnum(a,n);
selsort(a,n);
printnum(a,n);
}
