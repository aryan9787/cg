import matplotlib.pyplot as plt
# Defining region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute region code for a point(x, y)
def compute_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
    if y < y_min:      # below the rectangle
        code |= BOTTOM
    elif y > y_max:    # above the rectangle
        code |= TOP
    return code

# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def cohen_sutherland(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    # Compute region codes for P1, P2
    code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
    accept = False
    while True:
        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break
        else:
            # Some segment of line lies within the rectangle
            # At least one endpoint is outside the rectangle, pick it.
            code_out = code1 if code1 != 0 else code2
            # Find intersection point
            if code_out & TOP:
                # point is above the clip rectangle
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                # point is below the rectangle
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                # point is to the right of rectangle
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                # point is to the left of rectangle
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            # Now intersection point x, y is found
            # We replace point outside rectangle by intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, x_min, y_min, x_max, y_max)
    if accept:
        return ((x1, y1), (x2, y2))
    else:
        return None


def plot_line(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    plt.figure()
    plt.plot([x1, x2], [y1, y2], label='Line')
    plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], label='Clipping Window')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    x_min = int(input("Enter x_min: "))
    y_min = int(input("Enter y_min: "))
    x_max = int(input("Enter x_max: "))
    y_max = int(input("Enter y_max: "))
    result = cohen_sutherland(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
    if result is not None:
        print(f"The line from ({x1}, {y1}) to ({x2}, {y2}) clips to {result}.")
        plot_line(x1, y1, x2, y2, x_min, y_min, x_max, y_max)
        plot_line(result[0][0], result[0][1], result[1][0], result[1][1], x_min, y_min, x_max, y_max)
        
    else:
        print("The line doesn't lie within the rectangle.")