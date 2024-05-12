import numpy as np

def translate(point, tx, ty):
    transformation_matrix = np.array([[1, 0, tx],
                                      [0, 1, ty],
                                      [0, 0, 1]])
    return np.dot(transformation_matrix, point)

def rotate(point, theta):
    theta = np.radians(theta)
    transformation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                      [np.sin(theta),  np.cos(theta), 0],
                                      [0, 0, 1]])
    return np.dot(transformation_matrix, point)

def scale(point, sx, sy):
    transformation_matrix = np.array([[sx, 0, 0],
                                      [0, sy, 0],
                                      [0, 0, 1]])
    return np.dot(transformation_matrix, point)

# Example usage:
pointT = np.array([0, 0, 1])  # Homogeneous coordinates
pointR = np.array([4,3,1])
pointS = np.array([2,2,1])

point = translate(pointT, 2, 2)
print("After translation: ", point)

point = rotate(pointR, 45)
print("After rotation: ", point)

point = scale(pointS, 1.5, 0.5)
print("After scaling: ", point)