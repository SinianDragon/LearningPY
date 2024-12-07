import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import RegularPolygon  # 导入 RegularPolygon

# 方块网格
def draw_square_grid():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    for i in range(10):
        for j in range(10):
            ax.add_patch(plt.Rectangle((i, j), 1, 1, edgecolor='black', facecolor='none'))

    ax.set_xticks(np.arange(0, 11, 1))
    ax.set_yticks(np.arange(0, 11, 1))
    ax.grid(True)
    plt.title("Square Grid")
    plt.show()

# 六边形网格
def draw_hexagonal_grid():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # 六边形的高度和宽度
    hex_height = np.sqrt(3)
    hex_width = 2

    for i in range(5):
        for j in range(5):
            x = j * 3 + (i % 2) * 1.5
            y = i * hex_height
            ax.add_patch(RegularPolygon((x, y), 6, radius=1, edgecolor='black', facecolor='none'))

    ax.set_xticks(np.arange(0, 10, 3))
    ax.set_yticks(np.arange(0, 10, hex_height))
    ax.grid(True)
    plt.title("Hexagonal Grid")
    plt.show()

# 调用方块网格和六边形网格的绘制函数
draw_square_grid()
draw_hexagonal_grid()
