# Uses python3
def calc_fib(n):
	fib_n = [0] * (n + 1)
	fib_n[0] = 0
	if n >= 1:
		fib_n[1] = 1
	if n >= 2:
		for i in range(2, n + 1):
    			fib_n[i] = fib_n[i-1] + fib_n[i-2]
	return fib_n[n]

n = int(input())
assert n <= 45 and n >= 0
print(calc_fib(n))
