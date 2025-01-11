// #include<stdio.h>
// int main(){                                //addition of two numbers..........
//     int num1,num2;
//     printf("enter any number = ");
//     scanf("%d",&num1);
//     printf("enter any number = ");
//     scanf("%d",&num2);
//     printf("%d is sum of num1 and num2",num1+num2);
// }


// #include<stdio.h>
// int main(){
//     int num;
//     printf("enter any number = ");                      #code for check wheter the number is even or odd number ....
//     scanf("%d",&num);
//     if(num%2==0){
//         printf("num is even number");
//     } else{
//         printf("odd numnber");
//     }
// }


// #include<stdio.h>
// int main(){
//     int num;
//     printf("enter any number = ");
//     scanf("%d",&num);
//     if(num>0){
//         printf("%d is positive",num);
//     }                                      //CHCEK WHETHER THE NUMBER IS POSITIVE OR NEGGATIVE...
//     else if(num<0){
//         printf("%d is negative",num);
//     }
//     else{
//         printf("%d is neither positive nor negative",num);
//     }

//     return 0;
// 


// #include<stdio.h>

// int main() {
//     int i, num, factorial = 1;
//     printf("Enter a number: ");
//     scanf("%d", &num);
    
//     printf("Factorial of %d = ", num);                 //CODE FOR A FACTORIAL OF A GIVEN NUMBER.......
    
//     for (i = 1; i <= num; i++) {
//         factorial *= i;
//         if (i == 1) {
//             printf("%d", i);
//         } else {
//             printf("x%d", i);
//         }
//         if (i != num) {
//             printf("");
//         }
//     }
    
//     printf(" = %d\n", factorial);
    
//     return 0;
// }

// #include<stdio.h>
// int main(){
//     int a,b,c;
//     printf("enter value of a = ");
//     scanf("%d",&a);
//     printf("enter value of b = ");                  //check whether the triangle is isoseles or not .........
//     scanf("%d",&b);
//     printf("enter value of c = ");
//     scanf("%d",&c);
//     if(a==b && b==c && c==a){
//         printf("%d %d %d forms an equilateral triangle",a,b,c);
//     } else if (a==b || b==c || c==a){
//         printf(" %d %d %d isoseles traingle",a,b,c);
//     } else {
//         printf("scalene traingle");
//     }

// #include<stdio.h>
// int main(){
//     int n;
//     printf("enter a number = ");
//     scanf("%d",&n);
//     if(n>85 && n<100){
//         printf("Ex");
//     }
//     if(n>75 && n<85){
//         printf("A");
//     }
//     if(n>65 && n<75){
//         printf("B");
//     }                              //IF ELSE BASIC PROGRAM IIT BHUVANESHWER
//     if(n>55 && n<65){
//         printf("C");
//     }
//     if(n>45 && n<55){
//         printf("D");
//     }
//     if(n>35 && n<45){
//         printf("P");
//     }
//     if(n>0 && n<35){
//         printf("E");
//     }
//     if(n<0 && n>100){
//         printf("invalid number");
//     }
// }


// #include<stdio.h>
// int main(){
//     float f,c;char n;
//     printf("type F OR C = ");
//     scanf("%c",&n);
//     if(n=='F'){
//         printf("enter temperature in celsius = ");
//         scanf("%f",&c);                                    //converting temp to farenhiet or celscius... iit bhuvaneshwer
//         f=(1.8+32)*c;
//         printf("converting from celsius to fahrenheit is %f",f);
//     }
//     if(n=='C'){
//         printf("enter temperature in farenhiet = ");
//         scanf("%f",&f);
//         c=f/(1.8+32);
//         printf("converting from farenhiet to celsius is %f",c);
//     }

//     return 0;



// #include<stdio.h>
// int main(){
//     int a,b,c,sum,ang;
//     printf("enter a = ");
//     scanf("%d",&a);
//     printf("enter b = ");
//     scanf("%d",&b);
//     printf("enter c = ");
//     scanf("%d",&c);
//     sum=a+b+c;
//     if(sum>0 && sum==180){
//         printf("valid traingle");
//     }
//     else{
//         printf("invalid traingle");
//     }
//     if(sum>0 && sum==180){
//         printf("enter angle = ");
//         scanf("%d",&ang);
//         if(ang==90){
//             printf("right angle triangle");
//         }                                     //CORRECT TRAIANGLE IIT BHAVANESHWER......
//         else if(ang>90){
//             printf(" obtuse angle ");
//         }
//         else if(ang<90){
//             printf("acute angle");
//         }
//         else{
//             printf("not form a traingle");
//         }
// }
// }

// #include<stdio.h>
// int main(){
//     char a;
//     printf("enter the alphabet = ");
//     scanf("%c",&a);
//     if(a>='A' && a<='Z'){
//         printf("alphabet and uppercase");
//     }
//     if(a>='a' && a<='z'){                       //VOWEL OR UPPER CASE.............
//         printf("alphabet and lowercase");
//     }
//     if(a=='A'||a=='E'||a=='I'||a=='O'||a=='U'||a=='a'||a=='e'||a=='i'||a=='o'||a=='u'){
//             printf("vowel");
//         }else{
//             printf("consonant");
//         }
//     if(a>0 && a<9){
//         printf("digit");
//     }else{
//         printf("special character");
//     }
// }

// #include<stdio.h>
// int main(){
//     int n,s=0;
//     printf("enter a number = ");
//     scanf("%d",&n);
//     for(int i=0;i<=n;i++){
//         scanf("%d",&i);              //ex 1 in if else iit buvaneshwer
//     }
//     for(int i=0;i<=n;i++){
//         s=s+i*i;
//     }
//     printf("%d is there squares sum",s);
// }


#include<stdio.h>
#include<math.h>
int main(){
	int n,c=0,r,s=0,b;
	printf("enter any number =  ");
	scanf("%d",&n);
	int a=n;
	while(n>0){
		n/=10;
		c=c+1;
	}
    b=c;
	n=a;
	while(n>0){
		r=n%10;
		s=s+pow(r,c);
		printf("%d^%d",r,c);
        for(int i=1;i<b;i++){
            b=b-1;
            printf("+");
        }
        n=n/10;
	}
    printf("=");
	if(s==a){
		printf("a");
	}
}