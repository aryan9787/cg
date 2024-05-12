import matplotlib.pyplot as plt

def round(a):
    return int(a + 0.5)

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    Xinc = dx / steps
    Yinc = dy / steps
    x, y = x1, y1
    points = []
    for _ in range(steps):
        points.append((round(x), round(y)))
        x += Xinc
        y += Yinc
    return points

def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / dx if dx != 0 else float('inf')
    x, y = x1, y1
    points = []
    if slope <= 1:
        p = 2 * dy - dx
        for _ in range(dx):
            points.append((x, y))
            x += 1
            if p < 0:
                p = p + 2 * dy
            else:
                y += 1
                p = p + 2 * dy - 2 * dx
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            points.append((x, y))
            y += 1
            if p < 0:
                p = p + 2 * dx
            else:
                x += 1
                p = p + 2 * dx - 2 * dy
    return points

def plot_line(points):
    plt.figure(figsize=(5,5))
    plt.plot(*zip(*points), marker='o')
    plt.show()

if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("DDA:")
    points = dda(x1, y1, x2, y2)
    plot_line(points)
    print("Bresenham:")
    points = bresenham(x1, y1, x2, y2)
    plot_line(points)