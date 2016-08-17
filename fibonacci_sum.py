# Uses python3
import sys

def fibonacci_sum(n):
    fib_sum = 0
    if n >= 1:
    	fib_sum = 1
    prev = 1
    prevprev = 0
    if n > 1:
    	for i in range(2, (n + 1)):
    		fib_sum = (fib_sum+ prev + prevprev) % 10
    		temp = prevprev
    		prevprev = prev
    		prev = (prevprev + temp) % 10
    return fib_sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
