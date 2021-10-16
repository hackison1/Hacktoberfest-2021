#include <stdio.h>
int main() {
    char line[150];
    int i, n, alphabet, digit, space, special;

    alphabet = digit = space = special = 0;

    printf("Enter a line of string: ");
    scanf("%[^\n]",line);
	n = strlen(line);

    for (i = 0; i<n; ++i) {
        if ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= 'A' && line[i] <= 'Z')) {
            ++alphabet;
        } else if (line[i] >= '0' && line[i] <= '9') {
            ++digit;
        } else if (line[i] == ' ') {
            ++space;
        }
        else
        	++special;
    }

    printf("\nAlphabets: %d", alphabet);
    printf("\nDigits: %d", digit);
    printf("\nWhite spaces: %d", space);
    printf("\nSpecial Character: %d", special);
    return 0;
}
