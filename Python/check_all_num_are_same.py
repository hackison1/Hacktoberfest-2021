
# check if all the digits in the number N is the same or not

def checkSameDigits(N) :


	digit = N % 10;

	while (N != 0) :

		current_digit = N % 10;

		N = N // 10;

		if (current_digit != digit) :
			return "No";

	return "Yes";


if __name__ == "__main__" :

	N = 99999;
	print(checkSameDigits(N));
