import time

def sum_using_for_loop(n):
    total = 0
    for value in range(1, n + 1):
        total = total + value
    return total

n_values = [10, 100, 1000, 10000, 100000]

for n in n_values:
    start_time = time.time()
    result = sum_using_for_loop(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The sum of numbers from 1 to {n} is {result}. Execution time: {execution_time} seconds")