def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False

    # Check for factors from 2 up to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Divisor found

    return True  # No divisors found, it is prime


# --- Main block ---
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")
