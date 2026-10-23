# Practical 6: Introduction to Programming


# Q1. Create and access 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("First row:", matrix[0])
print("Element at row 2, column 3:", matrix[1][2])


# Q2. Matrix traversal
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row: print(item, end=" ")
    print()


# Q3. Sum of rows and columns
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Row sums:", [sum(row) for row in m])
print("Column sums:", [sum(m[r][c] for r in range(len(m))) for c in range(len(m[0]))])


# Q4. Matrix addition
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
result = [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]
print(result)


# Q5. Transpose of matrix
m = [[1, 2, 3], [4, 5, 6]]
print([list(row) for row in zip(*m)])


# Q6. NumPy array creation
import numpy as np
print(np.array([1, 2, 3]))
print(np.zeros((2, 3)))
print(np.ones((2, 2)))


# Q7. NumPy indexing and slicing
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element:", arr[1, 2])
print("First row:", arr[0, :])
print("Second column:", arr[:, 1])


# Q8. Array arithmetic
import numpy as np
a = np.array([1, 2, 3]); b = np.array([4, 5, 6])
print("Add:", a+b, "Subtract:", a-b, "Multiply elementwise:", a*b)


# Q9. Statistical operations
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(arr), "Median:", np.median(arr), "Standard deviation:", np.std(arr))


# Q10. Reshape array
import numpy as np
arr = np.arange(1, 13)
print(arr.reshape(3, 4))


# Q11. Matrix multiplication and transpose
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Matrix product:\n", a @ b)
print("Transpose:\n", a.T)


# Q12. Student marks analysis
import numpy as np
marks = np.array([[80, 75, 90], [65, 70, 72], [95, 88, 92]])
print("Average per student:", np.mean(marks, axis=1))
print("Highest mark:", np.max(marks), "Lowest mark:", np.min(marks))


# ==================== PRACTICE QUESTIONS ====================

# Q1. Calculate average soil moisture for each zone and find highest/lowest day.
import numpy as np
moisture = np.array([[45, 50, 48, 52, 47, 49, 51], [55, 53, 54, 52, 56, 57, 55], [38, 40, 42, 39, 41, 43, 44], [60, 62, 61, 63, 64, 62, 65]])
print("Zone averages:", moisture.mean(axis=1))
print("Highest moisture:", moisture.max(), "at zone/day:", np.unravel_index(moisture.argmax(), moisture.shape))
print("Lowest moisture:", moisture.min(), "at zone/day:", np.unravel_index(moisture.argmin(), moisture.shape))

# Q2. Analyze ICU temperatures for five patients.
temps = np.array([[98.6, 99.1, 100.2, 99.8, 98.9, 99.0], [97.8, 98.0, 98.4, 98.6, 98.2, 98.1], [101.2, 100.8, 101.5, 102.0, 101.7, 101.3], [99.4, 99.5, 99.6, 99.3, 99.2, 99.1], [98.7, 98.9, 99.0, 98.8, 98.6, 98.5]])
print("Highest per patient:", temps.max(axis=1))
print("Overall average:", temps.mean())
print("Critical patient index (0-based):", int(temps.max(axis=1).argmax()))

# Q3. Find busiest room, free slots, and occupancy percentage.
rooms = np.array([[1,1,0,1,0,1,1,0], [1,0,1,1,1,0,1,1], [0,1,1,0,1,1,0,1], [1,1,1,1,0,0,1,0], [0,0,1,1,1,1,1,1]])
occupied = int(rooms.sum())
print("Busiest room:", int(rooms.sum(axis=1).argmax()) + 1)
print("Free slots:", int(rooms.size - occupied))
print("Occupancy:", occupied / rooms.size * 100, "%")

# Q4. Invert brightness values in a grayscale image.
image = np.array([[120,135,140,150,160,170],[110,125,130,145,155,165],[100,115,120,135,145,155],[90,105,110,125,135,145],[80,95,100,115,125,135],[70,85,90,105,115,125]])
print(255 - image)

# Q5. Find shelf totals and maximum stock.
stock = np.array([[10,12,15,18,20,16,14,13,11,9],[8,10,12,14,16,18,20,22,24,26],[5,7,9,11,13,15,17,19,21,23],[30,28,26,24,22,20,18,16,14,12]])
print("Shelf totals:", stock.sum(axis=1))
print("Busiest shelf:", int(stock.sum(axis=1).argmax()) + 1)
print("Maximum bin stock:", int(stock.max()))
print("Column totals:", stock.sum(axis=0))

# Q6. Reshape vehicle counts and analyze traffic.
traffic = np.array([120,135,140,150,160,155,148,170,180,175,190,200,210,205,198,220,230,225,240,250,245,238,230,220])
traffic_matrix = traffic.reshape(3, 8)
print(traffic_matrix)
print("Peak slot (row, column):", np.unravel_index(traffic_matrix.argmax(), traffic_matrix.shape))
print("Least busy junction:", int(traffic_matrix.sum(axis=1).argmin()) + 1)
print("Average count:", traffic_matrix.mean())

# Q7. Reshape 60 heart-rate values into a 12 by 5 matrix.
heart_rate = np.array([72,74,73,75,76,74,73,72,78,80,82,79,77,76,75,74,73,72,71,70,69,68,67,66,72,74,76,78,80,82,84,83,81,79,77,75,74,73,72,71,70,69,68,67,66,65,72,74,76,78,80,82,84,86,88,85,83,81,79,77])
print(heart_rate.reshape(12, 5))

# Q8. Calculate weighted revenue using matrix multiplication.
sales = np.array([[100,120,130,140,150],[110,125,135,145,155],[90,100,110,120,130],[80,95,105,115,125],[70,85,95,105,115],[60,75,85,95,105],[50,65,75,85,95]])
weights = np.array([2, 3, 1, 4, 5])
print("Weighted revenue per store:", sales @ weights)

# Q9. Generate rainfall data and compare first and last 15 days.
rng = np.random.default_rng(7)
rainfall = rng.integers(20, 121, size=(8, 30))
print("First 15-day averages:", rainfall[:, :15].mean(axis=1))
print("Last 15-day averages:", rainfall[:, 15:].mean(axis=1))
print("Overall averages: first/last", rainfall[:, :15].mean(), rainfall[:, 15:].mean())

# Q10. Analyze a 10 by 10 terrain grid and extract its central 4 by 4 area.
rng = np.random.default_rng(10)
elevation = rng.integers(100, 501, size=(10, 10))
print("Highest ridge:", elevation.max())
print("Lowest valley:", elevation.min())
print("Average elevation:", elevation.mean())
print("Central 4x4 grid:", elevation[3:7, 3:7])
