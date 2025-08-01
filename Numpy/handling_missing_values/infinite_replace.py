import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr))  # Output: [False False  True False  True False]
cleaned_array = np.nan_to_num(arr, posinf=1000, neginf=-1000)  # Replace inf with specified values
print("Cleaned array:", cleaned_array)  # Output: [   1.    2. 1000.    4. -1000.    6.]
