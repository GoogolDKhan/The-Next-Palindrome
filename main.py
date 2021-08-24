# function will increment the number by one if it is not a palindrome or will return the number if it is a palindrome
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

# funtion to check whether the number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    n = int(input("Enter the number of test cases:\n"))
    numbers = []

    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        print(
            f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
