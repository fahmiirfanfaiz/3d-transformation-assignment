import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import time

def input_custom_points():
    vertices = []
    edges = []
    
    print("\nMasukkan titik-titik objek 3D Anda")
    print("Masukkan koordinat x y z untuk setiap titik, ketik 'done' ketika selesai")
    
    while True:
        point_input = input(f"Titik {len(vertices)} (x y z): ")
        if point_input.lower() == 'done':
            break
        try:
            x, y, z = map(float, point_input.split())
            vertices.append((x, y, z))
        except:
            print("Format salah, gunakan format: x y z")
    
    if len(vertices) < 2:
        print("Minimal 2 titik diperlukan, menggunakan kubus default")
        return create_cube()
    
    print("\nMasukkan edge/hubungan antar titik")
    print("Masukkan indeks titik yang terhubung (mulai dari 0), ketik 'done' ketika selesai")
    
    while True:
        edge_input = input(f"Edge {len(edges)} (indeks1 indeks2): ")
        if edge_input.lower() == 'done':
            break
        try:
            i, j = map(int, edge_input.split())
            if i < 0 or j < 0 or i >= len(vertices) or j >= len(vertices):
                print("Indeks tidak valid")
                continue
            edges.append((i, j))
        except:
            print("Format salah, gunakan format: indeks1 indeks2")
    
    if len(edges) == 0:
        print("Tidak ada edge yang dimasukkan, menghubungkan semua titik secara berurutan")
        edges = [(i, (i+1)%len(vertices)) for i in range(len(vertices))]
    
    return vertices, edges

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

def create_pyramid():
    vertices = [
        (0, 0, 1.5),  
        (-1, -1, 0),    
        (1, -1, 0),   
        (1, 1, 0),      
        (-1, 1, 0)      
    ]
    edges = [
        (0, 1), (0, 2), (0, 3), (0, 4),  
        (1, 2), (2, 3), (3, 4), (4, 1)    
    ]
    return vertices, edges

def create_prism():
    vertices = [
        (-1, -1, -1), (1, -1, -1), (0, 1, -1), 
        (-1, -1, 1), (1, -1, 1), (0, 1, 1)       
    ]
    edges = [
        (0, 1), (1, 2), (2, 0), 
        (3, 4), (4, 5), (5, 3),  
        (0, 3), (1, 4), (2, 5)   
    ]
    return vertices, edges

def create_sphere():
    vertices = [
        (0, 0, 1), (0, 0, -1),
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0)
    ]
    edges = [
        (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 4), (4, 3), (3, 5), (5, 2)
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
