"""
a=input("num1:")
b=input("num2:")
sum = int(a) + int(b)
print(sum)
"""
#fibonacci series
"""def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
for i in range(10):
  print(fibonacci(i))
"""
#factorial
"""def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);
num=4
print("factorial of" ,num,"is",factorial(num))"""


num = 16

# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")
