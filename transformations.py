import numpy as np

def translate(points, dx, dy, dz):
    matrix = np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])
    return apply_transformation(points, matrix)

def scale(points, sx, sy, sz):
    matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    return apply_transformation(points, matrix)

def rotate_x(points, angle):
    rad = np.radians(angle)
    matrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(rad), -np.sin(rad), 0],
        [0, np.sin(rad), np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    return apply_transformation(points, matrix)

def rotate_y(points, angle):
    rad = np.radians(angle)
    matrix = np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    return apply_transformation(points, matrix)

def rotate_z(points, angle):
    rad = np.radians(angle)
    matrix = np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return apply_transformation(points, matrix)

def shear(points, shx, shy):
    matrix = np.array([
        [1, shx, 0, 0],
        [shy, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return apply_transformation(points, matrix)

def apply_transformation(points, matrix):
    new_points = []
    for point in points:
        p = np.array([point[0], point[1], point[2], 1])
        transformed_p = matrix @ p
        new_points.append((transformed_p[0], transformed_p[1], transformed_p[2]))
    return new_points
