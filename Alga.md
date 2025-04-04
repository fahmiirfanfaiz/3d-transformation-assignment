# 3d-transformation-assignment
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, Slider
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection

class WireframeTransformationDemo:
    def __init__(self):
        # Membuat kubus sebagai objek wireframe dasar
        self.original_vertices = np.array([
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
        ])
        
        # Mendefinisikan tepi-tepi kubus
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        
        # Menyimpan vertices saat ini (yang bisa ditransformasi)
        self.current_vertices = self.original_vertices.copy()
        
        # Setup figure dan axes
        self.fig = plt.figure(figsize=(14, 8))
        self.fig.subplots_adjust(left=0.05, right=0.7)
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Inisialisasi plot wireframe
        self.draw_wireframe()
        
        # Setup panel kontrol
        self.setup_control_panel()
        
        # Transformasi yang aktif saat ini
        self.current_transform = 'translation'
    
    def draw_wireframe(self):
        """Menggambar wireframe berdasarkan vertices saat ini"""
        self.ax.clear()
        
        # Plot vertices
        self.ax.scatter(self.current_vertices[:, 0], 
                        self.current_vertices[:, 1], 
                        self.current_vertices[:, 2], 
                        color='r', s=50)
        
        # Plot edges
        for edge in self.edges:
            self.ax.plot([self.current_vertices[edge[0], 0], self.current_vertices[edge[1], 0]],
                         [self.current_vertices[edge[0], 1], self.current_vertices[edge[1], 1]],
                         [self.current_vertices[edge[0], 2], self.current_vertices[edge[1], 2]],
                         color='b', linewidth=2)
        
        # Set batas dan label axes
        self.ax.set_xlim([-2, 3])
        self.ax.set_ylim([-2, 3])
        self.ax.set_zlim([-2, 3])
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('3D Wireframe dengan Transformasi')
        
        # Atur sudut pandang
        self.ax.view_init(elev=30, azim=30)
        
        plt.draw()
    
    def setup_control_panel(self):
        """Setup panel kontrol untuk transformasi"""
        # Area untuk radio buttons
        radio_ax = plt.axes([0.75, 0.7, 0.2, 0.2])
        self.radio = RadioButtons(radio_ax, ('Translation', 'Rotation', 'Scaling', 'Shearing'))
        self.radio.on_clicked(self.set_transform)
        
        # Sliders untuk parameter transformasi
        self.slider_axes = []
        self.sliders = []
        
        # Slider untuk sumbu X
        ax_x = plt.axes([0.75, 0.6, 0.2, 0.03])
        slider_x = Slider(ax_x, 'X', -2.0, 2.0, valinit=0)
        slider_x.on_changed(self.update)
        self.sliders.append(slider_x)
        self.slider_axes.append(ax_x)
        
        # Slider untuk sumbu Y
        ax_y = plt.axes([0.75, 0.55, 0.2, 0.03])
        slider_y = Slider(ax_y, 'Y', -2.0, 2.0, valinit=0)
        slider_y.on_changed(self.update)
        self.sliders.append(slider_y)
        self.slider_axes.append(ax_y)
        
        # Slider untuk sumbu Z
        ax_z = plt.axes([0.75, 0.5, 0.2, 0.03])
        slider_z = Slider(ax_z, 'Z', -2.0, 2.0, valinit=0)
        slider_z.on_changed(self.update)
        self.sliders.append(slider_z)
        self.slider_axes.append(ax_z)
        
        # Button untuk reset
        reset_ax = plt.axes([0.75, 0.35, 0.2, 0.05])
        self.reset_button = Button(reset_ax, 'Reset')
        self.reset_button.on_clicked(self.reset)
    
    def set_transform(self, label):
        """Mengubah transformasi aktif saat ini"""
        self.current_transform = label.lower()
        
        # Reset sliders
        for slider in self.sliders:
            slider.set_val(0)
        
        # Menyesuaikan label slider untuk transformasi yang berbeda
        if self.current_transform == 'translation':
            self.sliders[0].label.set_text('X Translate')
            self.sliders[1].label.set_text('Y Translate')
            self.sliders[2].label.set_text('Z Translate')
        elif self.current_transform == 'rotation':
            self.sliders[0].label.set_text('X Rotate (°)')
            self.sliders[1].label.set_text('Y Rotate (°)')
            self.sliders[2].label.set_text('Z Rotate (°)')
            # Mengubah rentang untuk rotasi
            self.sliders[0].valmin = -180
            self.sliders[0].valmax = 180
            self.sliders[1].valmin = -180
            self.sliders[1].valmax = 180
            self.sliders[2].valmin = -180
            self.sliders[2].valmax = 180
        elif self.current_transform == 'scaling':
            self.sliders[0].label.set_text('X Scale')
            self.sliders[1].label.set_text('Y Scale')
            self.sliders[2].label.set_text('Z Scale')
            # Mengubah rentang untuk scaling
            self.sliders[0].valmin = 0.1
            self.sliders[0].valmax = 3.0
            self.sliders[0].set_val(1.0)
            self.sliders[1].valmin = 0.1
            self.sliders[1].valmax = 3.0
            self.sliders[1].set_val(1.0)
            self.sliders[2].valmin = 0.1
            self.sliders[2].valmax = 3.0
            self.sliders[2].set_val(1.0)
        elif self.current_transform == 'shearing':
            self.sliders[0].label.set_text('XY Shear')
            self.sliders[1].label.set_text('XZ Shear')
            self.sliders[2].label.set_text('YZ Shear')
            # Reset rentang untuk shearing
            self.sliders[0].valmin = -1.0
            self.sliders[0].valmax = 1.0
            self.sliders[1].valmin = -1.0
            self.sliders[1].valmax = 1.0
            self.sliders[2].valmin = -1.0
            self.sliders[2].valmax = 1.0
        
        plt.draw()
    
    def update(self, val):
        """Update wireframe berdasarkan transformasi yang dipilih"""
        # Reset ke vertices asli
        self.current_vertices = self.original_vertices.copy()
        
        # Mendapatkan nilai slider
        x_val = self.sliders[0].val
        y_val = self.sliders[1].val
        z_val = self.sliders[2].val
        
        # Menerapkan transformasi yang sesuai
        if self.current_transform == 'translation':
            self.translate(x_val, y_val, z_val)
        elif self.current_transform == 'rotation':
            self.rotate(x_val, y_val, z_val)
        elif self.current_transform == 'scaling':
            self.scale(x_val, y_val, z_val)
        elif self.current_transform == 'shearing':
            self.shear(x_val, y_val, z_val)
        
        # Menggambar ulang wireframe
        self.draw_wireframe()
    
    def translate(self, tx, ty, tz):
        """Translasi objek"""
        translation_matrix = np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ])
        
        # Menerapkan transformasi
        self.apply_transformation_matrix(translation_matrix)
    
    def rotate(self, rx, ry, rz):
        """Rotasi objek (dalam derajat)"""
        # Konversi dari derajat ke radian
        rx_rad = np.radians(rx)
        ry_rad = np.radians(ry)
        rz_rad = np.radians(rz)
        
        # Matriks rotasi X
        rotation_x = np.array([
            [1, 0, 0, 0],
            [0, np.cos(rx_rad), -np.sin(rx_rad), 0],
            [0, np.sin(rx_rad), np.cos(rx_rad), 0],
            [0, 0, 0, 1]
        ])
        
        # Matriks rotasi Y
        rotation_y = np.array([
            [np.cos(ry_rad), 0, np.sin(ry_rad), 0],
            [0, 1, 0, 0],
            [-np.sin(ry_rad), 0, np.cos(ry_rad), 0],
            [0, 0, 0, 1]
        ])
        
        # Matriks rotasi Z
        rotation_z = np.array([
            [np.cos(rz_rad), -np.sin(rz_rad), 0, 0],
            [np.sin(rz_rad), np.cos(rz_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        
        # Menggabungkan semua rotasi
        rotation_matrix = rotation_z @ rotation_y @ rotation_x
        
        # Menerapkan transformasi
        self.apply_transformation_matrix(rotation_matrix)
    
    def scale(self, sx, sy, sz):
        """Scaling objek"""
        scaling_matrix = np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])
        
        # Menerapkan transformasi
        self.apply_transformation_matrix(scaling_matrix)
    
    def shear(self, xy, xz, yz):
        """Shearing objek"""
        shearing_matrix = np.array([
            [1, xy, xz, 0],
            [0, 1, yz, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        
        # Menerapkan transformasi
        self.apply_transformation_matrix(shearing_matrix)
    
    def apply_transformation_matrix(self, matrix):
        """Menerapkan matriks transformasi ke vertices saat ini"""
        # Menambahkan kolom homogeneous coordinate
        homogeneous_vertices = np.hstack((self.current_vertices, np.ones((len(self.current_vertices), 1))))
        
        # Menerapkan transformasi
        transformed_vertices = homogeneous_vertices @ matrix.T
        
        # Konversi kembali ke koordinat 3D
        self.current_vertices = transformed_vertices[:, :3]
    
    def reset(self, event):
        """Reset objek ke posisi dan bentuk awal"""
        self.current_vertices = self.original_vertices.copy()
        
        # Reset semua slider
        for slider in self.sliders:
            if self.current_transform == 'scaling':
                slider.set_val(1.0)
            else:
                slider.set_val(0.0)
        
        # Menggambar ulang wireframe
        self.draw_wireframe()
    
    def show(self):
        """Menampilkan visualisasi"""
        plt.show()

if __name__ == "__main__":
    demo = WireframeTransformationDemo()
    demo.show()
