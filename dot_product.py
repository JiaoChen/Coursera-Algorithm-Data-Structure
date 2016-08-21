#Uses python3

import sys

def get_max(array):
	max = 0
	for i in range(len(array)):
		if array[i] > array[max]:
			max = i
	return max
 	
def max_dot_product(res, a, b):
    if len(a) == 0:
    	return res
    max_a_index = get_max(a)
    max_b_index = get_max(b)
    res += a[max_a_index] * b[max_b_index]
    del a[max_a_index]
    del b[max_b_index]
    return max_dot_product(res, a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(0, a, b))
    
