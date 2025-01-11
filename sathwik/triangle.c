// #include<stdio.h>
// int main(){
//     int n;
//     printf("no of rows = ");              //CODE FOR UPPER TRIANGLE
//     scanf("%d",&n);
//     printf("****Patern******\n");
//     for(int i=1;i<=n;i++){
//         for(int j=1;j<=n+1-i;j++){
//             printf("* ");
//         }
//         printf("\n");    
//     }
// }

// #include<stdio.h>
// int main(){
//     int n;
//     printf("no of rows = ");
//     scanf("%d",&n);                 // CODE FOR LOWER TRAINGLE
//     printf("****Patern******\n");
//     for(int i=1;i<=n;i++){
//         for(int j=1;j<=i;j++){
//             printf("* ");
//         }
//         printf("\n");    
//     }
// }

// 

// #include<stdio.h>
// int main(){
//     for(int i=1;i<=4;i++){
//         for(int j=1;j<=5-i;j++){    //CODE FOR UPPER NUMBER TRIANGLE
//             printf("%d",j);
//         }
//         printf("\n");
//     }
// }


// #include<stdio.h>
// int main(){
//     for(int i=1;i<=4;i++){
//         for(int j=1;j<=i;j++){    //CODE FOR LOWER NUMBER TRIANGLE
//             printf("%d",j);
//         }
//         printf("\n");
//     }
// }

// #include<stdio.h>
// int main(){
//     for(int i=1;i<=4;i++){
//         for(int j=1;j<=(2*(5-i))-1;j=j+2){         //CODE FOR UPPER ODD NUMBER TRAINGLE 
//             printf("%d ",j);
//         }
//         printf("\n");
//     }
// }

// #include<stdio.h>
// int main(){
//     for(int i=1;i<=4;i++){                    //CODE FOR UPPER TRIANGLE ALPHABETS
//         for(int j=1;j<=5-i;j++){
//             printf("%c ",j+64);
//         }
//         printf("\n");
//     }
// }

#include<stdio.h>
int main(){
    for(int i=1;i<=4;i++){                    //CODE FOR LOWER TRIANGLE ALPHABETS
        for(int j=1;j<=i;j++){
            printf("%c ",j+64);
        }
        printf("\n");
    }
}