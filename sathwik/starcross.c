#include<stdio.h>
int main(){
    for(int i=1;i<=5;i++){
        for(int j=1;j<=5;j++){               //CODE FOR STARCROSS PATTERN......
            if(i==j || i+j==6){
                printf("*");
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }
}