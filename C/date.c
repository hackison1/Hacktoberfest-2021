#include <stdio.h>
int a,yr,wk,days;
int convert(int ndays);
int convert(int ndays){
    yr=ndays/365;
    wk=(ndays%365)/7;
    days=ndays-yr*365-wk*7;
    printf("%d Years\t%d Weeks\t%d Days",yr,wk,days);
    return 0;
}
int main()
{
    printf("Enter number of days : ");
    scanf("%d",&a);
    convert(a);
	return 0;
}