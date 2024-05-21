def is_prime(n,i=2):
    if n<=2:
        return n == 2
    if n % i ==0:
        return False
    if i * i > n:
        return True
    return is_prime(n , i +1)

number=17
if is_prime(number):
    print(f"{number} is a prime number")

else:
    print(f"{number} is not a prime number")