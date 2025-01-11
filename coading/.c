//arrays

// #include<stdio.h>
// int main(){
//     int a[100],i,size;
//     printf("size = ");
//     scanf("%d",&size);
//     printf("array elements are");
//     for(i=0;i<=size;i++){
//         scanf("%d",&a[i]);
//     }
//      for(i=0;i<=size;i++){
//         printf("%d ",a[i]);
//     }
// }


// #include<stdio.h>
// int main(){
//     int arr[100],i,size;
//     printf("Input the number of elements  to store in the array : ");
//     scanf("%d",&size);
//     printf("Input %d number of elements in the array : \n",size);
//     for(i=0;i<size;i++){
//         printf("element - %d : ",i);
//         scanf("%d",&arr[i]);
//     }
//     printf("the values stored in the array are : ");
//     for(i=0;i<size;i++){
//         printf("%d  ",arr[i]);
//     }
//     printf("the values stored into the array in  reverse order ");
//     for(i=size-1;i>=0;i--){
//         printf("%d  ",arr[i]);
//     }
// }


// #include<stdio.h>
// int main(){
//     int a[100],i,n,sum=0;
//     scanf("%d",&n);
//     for(i=0;i<n;i++){
//         scanf("%d",&a[i]);
//     }
//     for(i=0;i<n;i++){
//         sum=sum+a[i];
//     }
//     printf("%d",sum);
// }


// #include<stdio.h>
// void main(){
//     int a[100],b[100],i,n;
//     scanf("%d",&n);
//      for(i=0;i<n;i++){
//         scanf("%d",&a[i]);
//     }
//     for(i=0;i<n;i++){
//         printf("%d ",a[i]);
//     }
//     for(i=0;i<n;i++){
//         b[i]=a[i];
//         printf("%d ",b[i]);
//     }
// }


// #include<stdio.h>
// int main(){
//     int a[100],size,count=0,i,j;
//     scanf("%d",&size);
//     for(int i=0;i<size;i++){
//         scanf("%d ",&a[i]);
//     }
//     for(int i=0;i<size;i++){
//         for(int j=i+1;j<size;j++){
//             if(a[i]==a[j])
//                 printf("%d is duplicate",a[i]);
//         }
//     }
// }


// #include<stdio.h>
// int main(){
//     int a[100],i,j,size,count;
//     printf("enter the size of an array = ");
//     scanf("%d",&size);
//     for(int i=0;i<size;i++){
//         scanf("%d",&a[i]);
//     }
//     for(int i=0;i<size;i++){
//     	count=1;
//         for(int j=0;j<size;j++){
//             if(i!=j){
//                 if(a[i]==a[j]){
//                     count=0;
//                     break;
//                 }
//             }
//         }
//         if(count==1){
//             printf("%d",a[i]);
//         }
//     }

// }


// #include<stdio.h>
// int main(){
//     int a[7]={3,4,5,7,1,2,9},i,j,temp;
//     for(int i=0;i<7;i++){
//         for(int j=i+1;j<7;j++){
//             if(a[i]>a[j]){
//                temp=a[i];
//                a[i]=a[j];
//                a[j]=temp;
//             }
//         }
//     }
//     for(int i=0;i<7;i++){
//         printf("%d ",a[i]);
//     }
// }

/*

Input the number of elements to be stored in the array :3
Input 3 elements in the array :
element - 0 : 25
element - 1 : 12
element - 2 : 43
Expected Output :
The frequency of all elements of an array :
25 occurs 1 times
12 occurs 1 times
43 occurs 1 times
*/

// #include<stdio.h>
// int main(){
//     int a[9]={1,2,1,3,4,2,2,4,5},count,i;
//     for(int i=0;i<9;i++){
//         count=1;
//         for(int j=i+1;j<9;j++){
//             if(a[i]==a[j]){
//                 count=count+1;
//                 a[j]=-1;
//             }
//         }
//         if(a[i]!=-1){
//         printf("%d occurs %d times\n",a[i],count);
//     }
//     }


// #include<stdio.h>
// int main(){
//     int a[100],i,j,max1,max2,size;
//     printf("size = ");
//     scanf("%d",&size);
//      for(int i=0;i<size;i++){
//         scanf("%d",&a[i]);
//     }
//     max1=a[0];
//     for(int i=0;i<size;i++){
//         if(a[i]>max1){
//             max1=a[i];
//         }
//     }
//     printf("first max is %d\n",max1);
//     max2=0;
//     for (int i = 0; i < size; i++) {
//     if (a[i] > max2 && a[i] != max1) {
//         max2 = a[i];
//     }
// }
//     printf("second max is %d\n",max2);
// }


#include<stdio.h>
int main(){
    int arr[100],key,size;
    printf("size=");
    scanf("%d",&size);
    printf("key=");
    scanf("%d",&key);
    printf("array elements\n");
    for(int i=0;i<=size;i++){
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<=size;i++){
        if(arr[i]==key){
            printf("%d is searched at the index of %d",key,i);
            break;
        }
    }

}