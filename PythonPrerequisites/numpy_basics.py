# -----------------------------------------
# 1. Importing NumPy
# -----------------------------------------
import numpy as np

# -----------------------------------------
# 2. Creating Arrays
# -----------------------------------------
arr1 = np.array([1, 2, 3])  # 1D array
arr2 = np.array([[1, 2], [3, 4]])  # 2D array

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# -----------------------------------------
# 3. Array Properties
# -----------------------------------------
print("Shape:", arr2.shape)
print("Data Type:", arr1.dtype)
print("Size (total elements):", arr2.size)

# -----------------------------------------
# 4. Useful Array Functions
# -----------------------------------------
zeros = np.zeros((2, 3))        # 2x3 array of 0s
ones = np.ones((3, 3))          # 3x3 array of 1s
identity = np.eye(3)            # 3x3 identity matrix
randoms = np.random.rand(2, 2)  # 2x2 array with random floats (0-1)

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity:\n", identity)
print("Randoms:\n", randoms)

# -----------------------------------------
# 5. Array Indexing and Slicing
# -----------------------------------------
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Slice:", arr[1:4])  # 20 to 40

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at [1, 2]:", matrix[1, 2])

# -----------------------------------------
# 6. Array Operations (Element-wise)
# -----------------------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Dot product:", np.dot(a, b))  # scalar

# -----------------------------------------
# 7. Reshaping and Flattening
# -----------------------------------------
arr = np.array([[1, 2], [3, 4], [5, 6]])
reshaped = arr.reshape(2, 3)
flattened = arr.flatten()

print("Reshaped to 2x3:\n", reshaped)
print("Flattened:", flattened)

# -----------------------------------------
# 8. Aggregate Functions
# -----------------------------------------
arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# -----------------------------------------
# 9. Logical Operations & Filtering
# -----------------------------------------
arr = np.array([10, 20, 30, 40])
print("Where > 25:", arr[arr > 25])  # Filter values

# -----------------------------------------
# 10. Save and Load Arrays
# -----------------------------------------
np.save("my_array.npy", arr)
loaded = np.load("my_array.npy")
print("Loaded from file:", loaded)

# -----------------------------------------
# Summary:
# - NumPy provides fast array operations.
# - Supports broadcasting, slicing, and mathematical operations.
# - Use `.shape`, `.dtype`, `.reshape()`, `np.sum()`, etc.
# - Use `.npy` for saving/loading arrays.
# -----------------------------------------