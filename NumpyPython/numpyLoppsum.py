import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Initialize sum variable
sum_elements = 0

# Loop through the array and accumulate the sum
for element in arr:
    sum_elements += element

print("Sum of array elements using loop:", sum_elements)
