/*
 Problem Statement : The Tribonacci sequence Tn is defined as follows:
                     T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
                     Given n, return the value of Tn.
*/

#include<bits/stdc++.h>
using namespace std;

// Function that returns the nth tribonacci number

int tribonacci(int n) {
    if (n < 3) return (n != 0);
    int dp[n + 1];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    } return dp[n];
}

// Main function

int main() {

    int n;
    cout << "Enter the number n : " << "\n";
    cin >> n;
    cout << "The value of Tn is : " << tribonacci(n);

    return 0;
}
