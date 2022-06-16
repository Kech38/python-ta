import sys
import os


def prime(s):
    
# A program to check if a number is prime or not
    # To take  input from the user

    num = int(input("Enter a value: "))

    # prime numbers are greater than 1
    if num > 1:

        for n in range(2, num):
            if (num % n) == 0:
                print(num, "is not a prime number")

                break

        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
