import numpy as np

# Part 1 - Overflow predictions
x = np.array([100, 200, 250], dtype=np.uint8)

print(x + 10)
print(x + 100)
print(x - 150)
print(x * 2)
print(x.astype(np.int16) + 100)
print(x * 1.5)
print((x * 1.5).dtype)

# Part 2 - OverflowError demonstration
# print(x + 300)  # Raises OverflowError: 300 is out of bounds for uint8

def add_safe(x, b):
    result = x.astype(np.int32) + b
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

print("Safe +100:", add_safe(x, 100))
print("Safe -150:", add_safe(x, -150))

# Bonus - int8 overflow
y = np.array([127], dtype=np.int8)
print("int8 overflow:", y + 1)