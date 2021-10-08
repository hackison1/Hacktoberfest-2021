/**
 * Author : Prashant Thakur (github : https://github.com/prashant-th18)
 * 
 * Task : 
 * We will be given a vector and number 'element'.
 * We are required to find the index of that number('element') if present in vector.
 */
#include <iostream> // For I/O operations
#include <vector> // For vector
#include <algorithm> // For sort function
#include <cassert>

// Function for Binary Search
int binarySearch(std :: vector<int>& v, const int& element)
{
	std :: sort(v.begin(), v.end()); // Vector is now sorted

	int si = 0, ei = (int)v.size() - 1; // si -> Starting Index,  ei -> Ending index
										// We want to find our number in [si, ei]

	while (si <= ei)
	{
		int mid;
		mid = (si + ei) / 2;
		if (v[mid] == element)
		{
			// number is found, therefore returning mid.
			return mid;
		}
		else if (v[mid] < element)
		{
			// number is greater than mid, so updating si to mid + 1, so that now we only need to
			// search from mid + 1 to ei
			si = mid + 1;
		}
		else
		{
			// number is less than mid, so updating ei to mid - 1, so that we only need to seach
			// from si to mid - 1
			ei = mid - 1;
		}
	}
	// Since si > ei, this means that number is not present.
	return -1;
}
// Test function for checking our binarySearch Function
void test()
{
	// Case - 1
	std :: vector<int> t1 = {4, 5, 2, 1, 7, 6};
	// Verifying that 5 is present at index 3 (0 - based)
	assert(binarySearch(t1, 5) == 3);
	// Verifying that 0 is not present
	assert(binarySearch(t1, 0) == -1);
	std :: cout << "All test cases run successfully\n";
}
int main()
{
	test();
	return 0; // Exiting the program
}