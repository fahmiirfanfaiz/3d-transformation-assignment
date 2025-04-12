import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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
