import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y1 = relu(x)


plt.plot(x, y1)
plt.ylim(-0.1, 1.1) #図で描画するy軸の範囲を指定
plt.show()