#include <stdio.h>
int calculateLength(char* ch) ;
int main()
{
    char name[20];
    scanf("%s",name);
    printf("%d",calculateLength(&name[0]));
	return 0;
}
int calculateLength(char* ch){
    int c=0;
    while(*ch!='\0'){
        c++;
        ch++;
    }
    return c;
}