#include <stdio.h>
int main()
{
   int Sum=0,Array[4]={1,2,3},i=0;
   for(i=1;i<4;i++){
        printf("%d\n",Array[i]);
        Sum+=Array[i];
   }

    printf("%d",Sum);
    return 0;
}