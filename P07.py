import numpy as np

def translate(point, tx, ty, tz):
    transformation_matrix = np.array([[1, 0, 0, tx],
                                      [0, 1, 0, ty],
                                      [0, 0, 1, tz],
                                      [0, 0, 0, 1]])
    return np.dot(transformation_matrix, point)

def rotate(point, ax, ay, az):
    ax, ay, az = np.radians(ax), np.radians(ay), np.radians(az)
    Rx = np.array([[1, 0, 0, 0],
                   [0, np.cos(ax), -np.sin(ax), 0],
                   [0, np.sin(ax), np.cos(ax), 0],
                   [0, 0, 0, 1]])
    Ry = np.array([[np.cos(ay), 0, np.sin(ay), 0],
                   [0, 1, 0, 0],
                   [-np.sin(ay), 0, np.cos(ay), 0],
                   [0, 0, 0, 1]])
    Rz = np.array([[np.cos(az), -np.sin(az), 0, 0],
                   [np.sin(az), np.cos(az), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    R = np.dot(Rz, np.dot(Ry, Rx))
    return np.dot(R, point)

def scale(point, sx, sy, sz):
    transformation_matrix = np.array([[sx, 0, 0, 0],
                                      [0, sy, 0, 0],
                                      [0, 0, sz, 0],
                                      [0, 0, 0, 1]])
    return np.dot(transformation_matrix, point)

def parallel_project(point):
    projection_matrix = np.array([[1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 1]])
    return np.dot(projection_matrix, point)

def perspective_project(point, d):
    projection_matrix = np.array([[1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 1, -1/d],
                                  [0, 0, 0, 1]])
    return np.dot(projection_matrix, point)

# Example usage:
point = np.array([1, 2, 3, 1])  # Homogeneous coordinates

point = translate(point, 2, 3, 4)
print("After translation: ", point)

point = rotate(point, 45, 45, 45)
print("After rotation: ", point)

point = scale(point, 2, 2, 2)
print("After scaling: ", point)

point = parallel_project(point)
print("After parallel projection: ", point)

point = perspective_project(point, 1)
print("After perspective projection: ", point)