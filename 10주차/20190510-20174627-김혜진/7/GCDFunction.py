def gcd(num1, num2):
    gcd = 1
    k = 2

    while k <= num1 and k <= num2:
        if (num1 % k == 0 and num2 % k == 0):
            gcd = k
        k+=1

        return gcd
