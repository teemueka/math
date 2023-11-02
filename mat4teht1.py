import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)

y1 = 2*x
y2 = 2*x + 3
y3 = -0.5*x - 4

plt.figure(figsize=(8,6))
plt.plot(x, y1, label='y=2x')
plt.plot(x, y2, label='y=2x+3')
plt.plot(x, y3, label='y=-1/2x-4')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.show()
