def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    number = int(input("Enter a number: "))

    if number == 1000:
        break

    if is_prime(number):
        print(f"{number} is prime.")