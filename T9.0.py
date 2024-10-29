# comput a finite product (n!=1*2*...*n)
n=3
product = 1
for i in range(1,n+1) :
    product *= i
print(product)