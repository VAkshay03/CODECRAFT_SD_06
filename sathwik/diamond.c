#include<stdio.h>
int main(){
    for(int i=1;i<=5;i++){
        for(int j=1;j<=6-i;j++){
            printf(" ");
        }
        for(int k=1;k<=i;k++){
            printf("* ");
        }
        printf("\n");
    }
    for(int i=1;i<=4;i++){
        for(int j=4;j>=5-i;j--){
             printf(" ");
        }
        printf(" ");
        for(int k=4;k>=i;k--){
            printf("* ");
        }
        printf("\n");
    }
}