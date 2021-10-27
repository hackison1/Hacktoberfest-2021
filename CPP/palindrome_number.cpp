// Checking palindrome number
#include <bits/stdc++.h>

using namespace std;

int palindrome_number(int n){

int sum=0, m;

        while(n>0)    
        {    
        m=n%10;    
        sum=(sum*10)+m;    
        n=n/10;    
        } 

return sum;

}

int main()  
{  
int n;    
cout << "Enter the number: ";    
cin >> n;

 int ans;
 ans = palindrome_number(n);    
     
if(n==ans)
cout << "Number is Palindrome";    
else    
cout << "Number is not Palindrome";  

  return 0;  
}  
