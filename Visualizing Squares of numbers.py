import matplotlib.pyplot as plt
import numpy as np

# Generate numbers from 1 to 1000
numbers = np.arange(1, 1001)
squares = numbers ** 2

# Create the plot
plt.figure(figsize=(12, 6))

# Line plot
plt.subplot(1, 2, 1)
plt.plot(numbers, squares, label='$y = x^2$', color='blue')
plt.title('Squares of Numbers (Linear Scale)')
plt.xlabel('Number (x)')
plt.ylabel('Square (x²)')
plt.grid(True)
plt.legend()

# Log-log plot to show the quadratic relationship
plt.subplot(1, 2, 2)
plt.loglog(numbers, squares, label='$y = x^2$', color='red')
plt.title('Squares of Numbers (Log-Log Scale)')
plt.xlabel('Number (x)')
plt.ylabel('Square (x²)')
plt.grid(True, which="both", ls="--")
plt.legend()

plt.tight_layout()
plt.show()