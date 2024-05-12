import matplotlib.pyplot as plt
import numpy as np

def mid_point_circle_draw(x_centre, y_centre, r):
    x = r
    y = 0
    points = []
    # Printing the initial point on the axes after translation
    points.append((x + x_centre, y + y_centre))
    # When radius is zero, only a single point is printed
    if r > 0:
        points.append((-x + x_centre, -y + y_centre))
        points.append((y + x_centre, x + y_centre))
        points.append((-y + x_centre, -x + y_centre))
    # Initialising the value of P
    P = 1 - r
    while x > y:
        y += 1
        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1
        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1
        # All the perimeter points have already been printed
        if x < y:
            break
        # Printing the generated point its reflection in the other octants after translation
        points.append((x + x_centre, y + y_centre))
        points.append((-x + x_centre, y + y_centre))
        points.append((x + x_centre, -y + y_centre))
        points.append((-x + x_centre, -y + y_centre))
        # If the generated point is on the line x = y then the perimeter points have already been printed
        if x != y:
            points.append((y + x_centre, x + y_centre))
            points.append((-y + x_centre, x + y_centre))
            points.append((y + x_centre, -x + y_centre))
            points.append((-y + x_centre, -x + y_centre))
    return points

def plot_circle(points):
    plt.figure(figsize=(5,5))
    plt.scatter(*zip(*points), marker='o')
    plt.show()

if __name__ == "__main__":
    x_centre = int(input("Enter x_centre: "))
    y_centre = int(input("Enter y_centre: "))
    r = int(input("Enter radius: "))
    points = mid_point_circle_draw(x_centre, y_centre, r)
    plot_circle(points)