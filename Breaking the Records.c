#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n,max=-1,min=-1; 
    scanf("%d",&n);
    int score[n],highest_score=0,lowest_score=0;
    for(int score_i = 0; score_i < n; score_i++)
    {
       scanf("%d",&score[score_i]);
        if (score[score_i]>max)
        {
            max=score[score_i];
            highest_score++;
        }
    }
    min=score[0];
    for (int score_i=1;score_i<n;score_i++)
     {   
        if (score[score_i]<min)
        {
            min=score[score_i];
            lowest_score++;
        }
     }
    printf("%d %d",highest_score-1,lowest_score);
    return 0;
}