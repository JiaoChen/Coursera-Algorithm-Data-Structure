# Uses python3
import sys

def gcd(a, b):
	smaller = min(a,b)
	larger = max(a,b)
	remainder = larger % smaller
	if remainder == 0:
		return smaller
	return gcd(smaller,remainder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
