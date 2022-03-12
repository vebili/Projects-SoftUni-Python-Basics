number = input()
counter = 0
prime = 0
non_prime = 0
while number != 'stop':
    number = int(number)
    if number < 0:
        print("Number is negative.")
    else:
        for x in range(1, number + 1):
            if number % x == 0:
                counter += 1
        if counter > 2:
            non_prime += number
        else:
            prime += number
    counter = 0
    number = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
