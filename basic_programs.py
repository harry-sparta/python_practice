# Program for Fibonacci numbers
    # Fibonacci numbers are in the following integer sequence
        # 0,1,1,2,3,5,8,13,21,34,55....
# Mathematically, it can be defined with the following relations:
    # F<n> = F<n-1> + F<n-2>
# There are 3 general methods to write this program:

# 1.) Recursion method
def fibonacci_recursion(num):
    if num < 0:
        print("Incorrect input - needs to be greater than 0")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)


# 2.) Dynamic method
fib_array=[0,1]
def fibonacci_dynamic(num):
    if num < 0:
        print("Incorrect input - needs to be greater than 0")
    elif num <= len(fib_array):
        return fib_array[num - 1]
    else:
        temp_fib = fibonacci_dynamic(num - 1) + fibonacci_dynamic(num - 2)
        fib_array.append(temp_fib)
        return temp_fib