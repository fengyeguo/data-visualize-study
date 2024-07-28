import numpy as np
import matplotlib.pyplot as plt

def bezier_curve(p0, p1, p2, num_points=100):
    t = np.linspace(0, 1, num_points)
    curve = (1 - t)[:, None] ** 2 * p0 + 2 * (1 - t)[:, None] * t[:, None] * p1 + t[:, None] ** 2 * p2
    return curve

# 控制点
p0 = np.array([0, 0])
p1 = np.array([1, 2])
p2 = np.array([2, 0])

# 计算贝塞尔曲线
curve = bezier_curve(p0, p1, p2)

# 绘制曲线和控制点
plt.plot(curve[:, 0], curve[:, 1], label='Bezier Curve')
plt.scatter([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color='red')
plt.legend()
plt.title('Quadratic Bezier Curve')
plt.show()