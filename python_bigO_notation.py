# Big O notation is a mathematical notation that describes the upper bound or worst-case scenario for the time complexity of an algorithm. It helps us answer questions like:

# Big O notation is written as "O(f(n))," where "f(n)" is a function that represents the relationship between the input size (usually denoted as "n") and the algorithm's runtime or resource usage.

# ---------- EXAMPLES --------------------- #

# O(1) - Constant Time
# Example: Accessing an element in an array by its index.
def accessElement(arr,index):
    return arr[index]

# No matter how large the array is, accessing an element by its index takes the same amount of time. The runtime is constant, and we denote it as O(1).

# O(n) - Linear Time
# Algorithms with linear time complexity have a runtime that grows linearly with the size of the input data. This means that if the input data doubles in size, the runtime also doubles.

def linearSearch(arr,target):
    for item in arr:
        if item == target:
            return True
    return False

# As the size of the list (arr) increases, the number of iterations the loop performs also increases linearly. Therefore, this algorithm has a time complexity of O(n).



