#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int n,rank=0; 
    scanf("%d",&n);
    int scores[n];
    for(int scores_i = 0; scores_i < n; scores_i++)
    {
       scanf("%d ",&scores[scores_i]);
        if(scores!=0)
        {
            if (scores[scores_i]!=scores[scores_i-1] )
                {
                   rank++;
            }
        }
        else
            rank++;
         
    }
    int a=0,original_scores[rank];
    for(int i=0;i<n;i++)
       {
        if(scores[i]!=scores[i+1])
            original_scores[a++]=scores[i];
       }
    int m; 
    scanf("%d",&m);
    int alice[m];
    for(int alice_i = 0; alice_i < m; alice_i++)
    {
       scanf("%d ",&alice[alice_i]);
    }
    int temp2=rank-1;
    for(int i=0;i<m;i++)
        {
        for(int j=temp2;j>=0;j--)
       {
            if(alice[i]<original_scores[j])
                {
                printf("%d\n",j+2);
                temp2=j;
                break;
            }
            if(alice[i]==original_scores[j])
                {
                printf("%d\n",j+1);
                temp2=j;
                break;
            }
            if(j==0)
               printf("%d\n",j+1);
        }
    }
    return 0;
}