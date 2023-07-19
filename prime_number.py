def number_is_prime(number: int):
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
        return True


def range_checking():
    low_limit = 0
    high_limit = 100001
    user_number = int(input("Enter your number: "))
    while user_number not in range(low_limit, high_limit):
        user_number = int(input(f"Incorrect number, should be from {low_limit} to {high_limit} \nEnter your number: "))
    return user_number


checking_number = range_checking()
start_prime_numbers = [1, 2, 3, 5, 7]
if checking_number in start_prime_numbers or number_is_prime(checking_number):
    print("The number is prime.")
else:
    print("The number is composite.")
