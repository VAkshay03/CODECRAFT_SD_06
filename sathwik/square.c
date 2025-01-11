#include<stdio.h>
int main(){
    int n,rows;
    printf("no of rows = ");
    scanf("%d",&rows);
    printf("n = ");
    scanf("%d",&n);
    printf("PATTERN IS....\n");
    //outer loop signifies the no of lines
    for(int i=1;i<=rows;i++){   
        //inner loop signifies the no of stars in the line   
        for(int j=1;j<=n;j++){  
            printf("* "); 
        }
        printf("\n");//after every line its enters to new line
    }
}