c=0

def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
                break
        else:
            return True

for i in range(0,101):
    if isPrime(i):
        c+=1

print(c)