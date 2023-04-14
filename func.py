def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def prime_range(num):
    for i in range(2,num+1):
        if isprime(i)==True:
            yield i

def prime_factors(n):
    divisor=2
    lst=[]
    while divisor<=n:
        if n%divisor==0:
            n/=divisor
            lst.append(divisor)
        else:
            divisor+=1
    return lst
