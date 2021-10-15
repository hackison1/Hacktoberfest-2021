#include<iostream>
using namespace std;
//written by pankaj
int main(){

    int n;
    cin >> n;
    while (n > 0){
        cout << n%2;
        n = n/2;
    }

    return 0;
}
