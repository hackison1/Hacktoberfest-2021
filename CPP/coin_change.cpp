/*
 Problem Statement : Given a value N, find the number of ways to make change for N cents,
					 if we have infinite supply of each of S = { S1, S2, .. , SM } valued coins.
*/

#include<bits/stdc++.h>
using namespace std;

// Function to find the number

long long int count( int S[], int m, int n ) {

	long long int dp[m + 1][n + 1];
	for (int i = 0; i <= n; i++) dp[0][i] = 0;
	for (int i = 0; i <= m; i++) dp[i][0] = 1;
	for (int i = 1; i <= m; i++) {
		for (int j = 1; j <= n; j++) {
			if (S[i - 1] <= j) {
				dp[i][j] = dp[i][j - S[i - 1]] + dp[i - 1][j];
			} else dp[i][j] = dp[i - 1][j];
		}
	} return dp[m][n];
}

// Main function

int main() {

	int n, m;
	cout << "Enter the value of N and M: " << "\n";
	cin >> n >> m;
	int arr[m];
	cout << "Enter the values of S1, S2, ....SM : " << "\n";
	for (int i = 0; i < m; i++)
		cin >> arr[i];
	cout << "Total number of required ways is : " << count(arr, m, n) << endl;

	return 0;
}
