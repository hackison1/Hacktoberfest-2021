#include<stdio.h>
#include<stdlib.h>
void readmatrix(int a[][100],int m,int n)
{
int i,j;
printf("enter the elements row by row\n");
for(i=0;i<m;i++)
for(j=0;j<n;j++)
scanf("%d",&a[i][j]);
}
void displaymatrix(int a[][100],int m,int n)
{
int i,j;
for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
printf("%5d",a[i][j]);
printf("\n");
}
}
void addmatrix(int a[][100],int b[][100],int m,int n)
{
int i,j,c[100][100];
for(i=0;i<m;i++)
for(j=0;j<n;j++)
c[i][j]=a[i][j]+b[i][j];
printf("Sum of matrix...\n");
displaymatrix(c,m,n);
}
void transpose(int a[][100],int m,int n)
{
int i,j,c[100][100];
for(i=0;i<m;i++)
for(j=0;j<n;j++)
c[j][i]=a[i][j];
displaymatrix(c,n,m);
}
void multmatrix(int a[][100],int b[][100],int m1,int n1,int n2)
{
int c[100][100],i,j,k;
// Multiply the two
for (i = 0; i < m1; i++) {
for (j = 0; j < n2; j++) {
c[i][j] = 0;
for (k = 0; k < n1; k++)
c[i][j] += a[i][k] * b[k][j];
}
}
printf("Product of matrix...\n");
displaymatrix(c,m1,n2);
}
int main()
{ int a[100][100],b[100][100],m1,n1,m2,n2,op;
printf("Enter the size of the matrix A row,column\n");
scanf("%d%d",&m1,&n1);
printf("Enter Matrix A\n");
readmatrix(a,m1,n1);
printf("Enter the size of the matrix B row column\n");
scanf("%d%d",&m2,&n2);
printf("Enter Matrix B\n");
readmatrix(b,m2,n2);
printf("Matrix A..\n");
displaymatrix(a,m1,n1);
printf("Matrix B..\n");
displaymatrix(b,m2,n2);
while(1)
{

printf("1.add 2.multiply 3.transpose 4.exit \n");
printf("Enter the option.....:");
scanf("%d",&op);
switch(op)
{
case 1: if(m1==m2 && n1==n2)
addmatrix(a,b,m1,n1);
else
printf("Incompatable matrix...cannot add..\n");
break;
case 2:if(n1==m2)
multmatrix(a,b,m1,n1,n2);
else
printf("Incompatable matrix...cannot mutliply..\n");
break;
case 3: printf("Transpose of A..\n");
transpose(a,m1,n1);
printf("Transpose of B..\n");
transpose(b,m2,n2);
break;
case 4: exit(0);
}
}
}

CR, [20.10.21 13:44]
/*Program to read and print data of n employees (name,employee_id,salary)using structure and display information.
NAME:SHERIN ALOSIOUS
CLASS:EC-B
ROLL NO:37*/
#include<stdio.h>
struct Employee
 {
   char Name[20];
   int Emp_id;
   float Salary;
  };
int main()
{
    struct Employee emp[20];
    int i,n;
    printf("Enter the no. of Employee: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
      printf("Enter full name: ");
      scanf("%s",emp[i].Name);
      printf("Enter employee id: ");
      scanf("%d",&emp[i].Emp_id);
      printf("Enter salary: ");
      scanf("%f",&emp[i].Salary);
     }
     printf("Display Information\n");
     for(i=0;i<n;i++)
     {
      printf("Name: %s\n",emp[i].Name);
      printf("Employee Id:%d\n",emp[i].Emp_id);
      printf("Salary: %.2f\n",emp[i].Salary);
      }
  return 0;
 }

CR, [20.10.21 13:45]
/*Program to read two input each representing the distances between two points in the Eucliean space,store these in structural variables and add the two distance values.
Name: Sherin Alosious
Class:ECE B
Roll no:37*/
#include<stdio.h>
int main()
{
struct euclidian
{
int distance;
  }
  d,d1;
{
 int sum=0;
   printf("\nEnter the distance between first two points:");
   scanf("%d",&d.distance);
   printf("\nEnter the distance between another two points:");
   scanf("%d",&d1.distance);
   sum=d.distance+d1.distance;
   printf("\nTotal distance = %d",sum);
   return 0;
    }
}

CR, [20.10.21 13:45]
/*C program to declare a union containing 5 string variables (Name, House Name, City Name, State and Pincode) each with a length of C_SIZE (user defined constant).
Then, read and display the address of a person using a variable of the union.
NAME: SHERIN ALOSIOUS
ROLL NO: 37
CLASS: EC-B*/
#include <stdio.h>
#include <string.h>
#define C_SIZE 50
union Address
{
       char name[C_SIZE];
       char hname[C_SIZE];
       char cityname[C_SIZE];
       char state[C_SIZE];
       char pin[C_SIZE];
};

int main()
{
    union Address record1;
  
    printf("Enter name:");
    scanf("%[^\n]",record1.name);
    getchar();
    printf("Enter house name:");
    scanf("%[^\n]",record1.hname);
    getchar();
    printf("Enter city name:");
    scanf("%[^\n]",record1.cityname);
    getchar();
    printf("Enter state name:");
    scanf("%[^\n]",record1.state);
    getchar();
    printf("Enter pin:");
    scanf("%[^\n]",record1.pin);

    printf("....Union record1 values ....\n");
    printf(" Name         : %s \n", record1.name);
    printf(" House Name  : %s \n", record1.hname);
    printf(" City Name    : %s \n", record1.cityname);
    printf(" State name   : %s \n", record1.state);
    printf(" Pin          : %s \n\n", record1.pin);
  return 0;  
 }

CR, [20.10.21 13:45]
/*C program to declare a union containing 5 string variables (Name, House Name, City Name, State and Pincode) each with a length of C_SIZE (user defined constant).
Then, read and display the address of a person using a variable of the union.
NAME: SHERIN ALOSIOUS
ROLL NO: 37
CLASS: EC-B*/
#include <stdio.h>
#include <string.h>
#define C_SIZE 50
union Address
{
       char name[C_SIZE];
       char hname[C_SIZE];
       char cityname[C_SIZE];
       char state[C_SIZE];
       char pin[C_SIZE];
};

int main()
{
    union Address record1;
  
    printf("Enter name:");
    scanf("%[^\n]",record1.name);
    getchar();
    printf("Enter house name:");
    scanf("%[^\n]",record1.hname);
    getchar();
    printf("Enter city name:");
    scanf("%[^\n]",record1.cityname);
    getchar();
    printf("Enter state name:");
    scanf("%[^\n]",record1.state);
    getchar();
    printf("Enter pin:");
    scanf("%[^\n]",record1.pin);

    printf("....Union record1 values ....\n");
    printf(" Name         : %s \n", record1.name);
    printf(" House Name  : %s \n", record1.hname);
    printf(" City Name    : %s \n", record1.cityname);
    printf(" State name   : %s \n", record1.state);
    printf(" Pin          : %s \n\n", record1.pin);
  return 0;  
 }
