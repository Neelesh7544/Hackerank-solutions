#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>



int main(){
    int n;int i = 0;
    int min_a = 100;
    int m;int factor = 0;
    int max_b = 0;
    scanf("%d %d",&n,&m);
    int a[n],b[m];
    for(int a_i = 0;a_i < n;a_i++)
    {
       scanf("%d",&a[a_i]);
       if( a[a_i] <= min_a ) 
           min_a = a[a_i];
        
    }
    for(int b_i = 0;b_i < m;b_i++)
    {
       scanf("%d",&b[b_i]);
        if(b[b_i] > max_b) 
            max_b = b[b_i];
    }
   
   for(int i = min_a; i <= max_b ;++i )
   {
        int sum = 0;
    for (int j = 0; j < n;j++)
        sum +=i%a[j];
   for(int k = 0; k <m ;k++)
       sum +=b[k]%i;
       if(sum == 0)
        ++factor;
   }
   
    
    printf("%d",factor);
    
    return 0;
}