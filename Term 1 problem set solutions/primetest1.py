
def is_prime(n):
    if n==2:
        return True
    if (n>2 and n%2==0):
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

print(is_prime(909090909090909091))