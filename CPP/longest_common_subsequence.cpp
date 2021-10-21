// Problem Statement : Given two strings, find the longest common subsequence

#include<bits/stdc++.h>
const int mod = 1e9 + 7;
using namespace std;

// Function to find LCS

int lcs(int x, int y, string s1, string s2) {
    int dp[x + 1][y + 1];
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i <= x; i++) {
        for (int j = 0; j <= y; j++) {
            if (i == 0 || j == 0) dp[i][j] = 0;
            else {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                }
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    } return dp[x][y];
}

// Main function

int main() {

    int n, k, x, y;
    cout << "Enter the lengths of strings : " << "\n";
    cin >> x >> y;
    string s1, s2;
    cout << "Enter the strings : " << "\n";
    cin >> s1 >> s2;
    cout << "The length of longest commmon subsequence is : " << lcs(x, y, s1, s2) << endl;

    return 0;
}
