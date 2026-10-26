import numpy as np

# Part 1 - Create a black grayscale image
black_image = np.zeros((100, 200), dtype=np.uint8)

print(black_image.shape)


# Part 2 - Create a white grayscale image
white_image = np.full((100, 200), 255, dtype=np.uint8)

print(white_image.shape)

# Part 3 - Create a solid red RGB image
color_image = np.full((100, 200, 3), [255, 0, 0], dtype=np.uint8)

print(color_image.shape)

# Part 4 - Print image properties
for name, image in [
    ("Black", black_image),
    ("White", white_image),
    ("Color", color_image)
]:
    print(name)
    print("shape:", image.shape)
    print("ndim:", image.ndim)
    print("size:", image.size)
    print("nbytes:", image.nbytes)

    # Part 5 - Calculate image memory usage

# 1920 x 1080 color image
hd_image = np.zeros((1080, 1920, 3), dtype=np.uint8)

print("1920x1080 image:", hd_image.nbytes, "bytes")

# 12-megapixel color image
image_12mp = np.zeros((3000, 4000, 3), dtype=np.uint8)

print("12 MP image:", image_12mp.nbytes, "bytes")

# Part 6 - Array operations
b = np.arange(12).reshape(3, 4)

print(b)
print(b.sum())
print(b.sum(axis=0))
print(b.sum(axis=1))
print(b[2, 3], b[-1, -1])