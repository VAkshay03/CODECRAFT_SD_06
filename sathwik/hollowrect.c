#include<stdio.h>
int main(){
    for(int i=1;i<=6;i++){                           //CODE FOR HOLLOW RECTANGLE
        for(int j=1;j<=6;j++){
            if(i==1 || i==6 || j==1 || j==6){
                printf("*");
            }else{
                printf(" ");
            }
        }printf("\n");
    }
}