import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import time

def create_cube():
    vertices = [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
    ]
    
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
    return vertices, edges

def plot_wireframe(vertices, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for edge in edges:
        p1, p2 = edge
        x_values = [vertices[p1][0], vertices[p2][0]]
        y_values = [vertices[p1][1], vertices[p2][1]]
        z_values = [vertices[p1][2], vertices[p2][2]]
        ax.plot(x_values, y_values, z_values, 'bo-')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def animate_transformation(start_vertices, end_vertices, edges, steps=20, delay=0.05):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for step in range(1, steps + 1):
        ax.clear()
        intermediate = []
        for p1, p2 in zip(start_vertices, end_vertices):
            x = p1[0] + (p2[0] - p1[0]) * step / steps
            y = p1[1] + (p2[1] - p1[1]) * step / steps
            z = p1[2] + (p2[2] - p1[2]) * step / steps
            intermediate.append((x, y, z))

        for edge in edges:
            i, j = edge
            x_vals = [intermediate[i][0], intermediate[j][0]]
            y_vals = [intermediate[i][1], intermediate[j][1]]
            z_vals = [intermediate[i][2], intermediate[j][2]]
            ax.plot(x_vals, y_vals, z_vals, 'bo-')

        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_zlim([-5, 5])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.pause(delay)
    plt.show()
