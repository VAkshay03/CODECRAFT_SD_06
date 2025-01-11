// #include<stdio.h>
// int main(){
//     int n;
//     printf("enter a number=  ");
//     scanf("%d",&n);                    //code to enter the numbers upto to nth term
//     int i=1;
//     while(i<=n){
//         printf("%d",i);
//         i++;
//     }
// }

// #include<stdio.h>
// int main(){
//     int i,n;
//     printf("value of i = ");
//     scanf(" %d", &i);
//     printf("n =  ");
//     scanf("%d",&n);          //code for reverse order naturral numbers.......
//     while(i>=n){
//         printf("%d ", i);
//         i--;
//     }
// }

// #include<stdio.h>
// int main(){
//     char a=97,n=122;                      ascii values of the alphabets........
//     while(a<=n){
//         printf("%c ",a);
//         a++;
//     }
// }

// #include<stdio.h>
// int main(){
//     int i,j;
//     printf("i = ");
//     scanf("%d",&i);
//     printf("j = ");                  //code even numbers between 1 to 100 using while loop.....
//     scanf("%d",&j);
//     while(i<=j){
//         if(i%2==0){
//             printf("%d ",i);
//         }
//         i++;
//     }
//}

// #include<stdio.h>
// int main(){
//     int l,f;
//     printf("enter value of f = ");
//     scanf("%d",&f);
//     l=f%10;                             code for to find last and first digit.....
//     printf("last digit is %d",l);
//     while(f>10){
//         f=f/10;
//     }
//     printf(" first digit is %d",f);
// }

// #include<stdio.h>
// int main(){
//     int n;
//     printf("enter n = ");
//     scanf("%d",&n);
//     int c=0;
//     int a=n;                         //counting number of digits ina given number....
//     while(n>0){
//         n/=10;
//         c++;
//     }
//     printf("nnumber of digits present in %d is %d",a,c);
// }

// #include<stdio.h>
// int main(){
//     int n,r;
//     printf("enter a number = ");
//     scanf("%d",&n);
//     while(n>0){                  //reverse of a number....
//         int r=n%10;
//         printf("%d",r);
//         n/=10;
        
//     }
    
// }

// #include<stdio.h>
// int main(){
//     int n,r,s=0;
//     scanf("%d",&n);
//     while(n>0){
//         r=n%10;                    //sum of digits of a number........
//         n/=10;
//         s=s+r;
//     }
//     printf("sum of digits of a number is  %d",s);
// }

// #include<stdio.h>
// int main(){
//     int n,r,s=1;
//     scanf("%d",&n);
//     while(n>0){
//         r=n%10;                    //product of digits of a number........
//         n/=10;
//         s=s*r;
//     }
//     printf("product of digits of a number is  %d",s);
// }

// #include<stdio.h>
// int main(){
//     int n,r,s=0;
//     printf("enter number = ");
//     scanf("%d",&n);
//     int a=n;
//     while(n>0){
//         r=n%10;                 //palindrome.........
//         n=n/10;
//         s=r+(s*10);
//     }
//     n=a;
//     if(n==s){
//         printf("palindrome");
//     }
// }
// #include<stdio.h>
// #include<math.h>
// int main(){
//     int n,c=0,d,m,swap;
//     printf("enter a number = ");
//     scanf("%d",&n);
//     int a=n;
//     while(n>0){
//         n=n/10;                     //code for swapping ..........first and last digit...
//         c++;
//     }
//     n=a;
//     d=n/pow(10,(c-2));
//     m=pow(10,(c-2));
//     swap=n%10;
//     swap=swap*pow(10,(c-1))+(d%m*pow(10,c-(c-1)))+n/pow(10,((c-1)));
//     printf("%d",swap);
// }


// #include<stdio.h>
// int main(){
// 	for(int i=0;i<=255;i++){          //ASCII VALUES.....
// 		printf("%c=%d\n",i,i);
// 	}
// }

// #include<stdio.h>
// #include<math.h>
// int main(){
// int n1,n2,power;
// printf("n1 = ");       //code for calculating the power........
// scanf("%d",&n1);
// printf("n2 = ");
// scanf("%d",&n2);
// power=pow(n1,n2);
// printf("%d",power);
// }

// #include<stdio.h>
// int main(){
//     int n;
//     printf("enter a number = ");
//     scanf("%d",&n);                      to calculate factors of a given number.....
//     printf("factors of %d are ",n);
//     for(int i=1;i<=n;i++){
//         if(n%i==0){
//             printf("%d ",i);
//         }
//     }
// }


// #include<stdio.h>
// int main(){
//     int n,p=1;
//     printf("enter a number = ");
//     scanf("%d",&n);
//     for(int i=1;i<=n;i++){      factorial of a number.......
//         p=p*i;
//         printf("%d ",p);
//     }
// }


// #include<stdio.h>
// int main(){
//     int c=0,n;
//     printf("enter value of n = ");
//     scanf("%d",&n);
//     for(int i=1;i<=n;i++){
//         if(n%i==0){                
//             c=c+1;
//         }
//     }              checking primr or not.......
//     if(c==2){
//         printf("%d is prime number",n);
//     }
//     else{
//         printf("%d is a composite number",n);
//     }
// }
