#include <stdio.h>
int main()
{
    int a;
    int b;
    int c;
    
    printf("Enter 1st Number : ");
    scanf("%d",&a);
    printf("Enter 2nd Number : ");
    scanf("%d",&b);
    printf("Enter 3rd Number : ");
    scanf("%d",&c);

    int max = a;
    char maxvariable = 'a';

    if (b > max)
    {
        max = b;
        maxvariable = 'b';
    }

    if (c > max)
    {
        max = c;
        maxvariable = 'c';
    }
    printf("The Greatest Integer is : %c = %d", maxvariable, max);
    return 0;
}

