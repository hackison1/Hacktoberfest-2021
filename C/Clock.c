/*#include <stdio.h>
#include <time.h>
int main(){
    int hour, minute, second;
    hour=minute=second=0;
    while(1)
    {    
        printf("%02d : %02d : %02d \n",hour,minute,second);
        second++;
        if(second==59){
            minute+=1;
            second=0;
        }
        if(minute==60){
            hour+=1;
            minute=0;
        }
        if(hour==24){
            hour=0;
            minute=0;
            second=0;
        }    
        sleep(1);
    }
    return 0;
}
*/
#include <stdio.h>
#include <time.h>
int main(){
    int hour=0, minute=0, second=0;
    
	printf("\n\n\t\tRunning Digital Clock: \n\n\n");
    while(1){    
        printf("\r \t\t%d hr : %d m : %d s",hour,minute,second);
        second++;
            if(second==59){
            minute++;
            second=0;
        }
        if(minute==59){
            hour++;
            minute=0;
            second=0;
        }
        if(hour==24){
            hour=0;
            minute=0;
            second=0;
        } 
		sleep(1);   
    }
}