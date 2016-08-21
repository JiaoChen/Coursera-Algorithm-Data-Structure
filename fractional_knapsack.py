# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_value = [float(x)/float(y) for x,y in zip(values,weights)]
    index = [unit_value.index(x) for x in sorted(unit_value,reverse = True)]
    for i in index:
        value += min(capacity, weights[i]) * unit_value[i]
        capacity = capacity - min(capacity, weights[i])
        if capacity == 0:
            return value
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
