from transformations import *
from wireframe import create_cube, plot_wireframe, animate_transformation

def main():
    original_vertices, edges = create_cube()
    vertices = original_vertices.copy()
    history = []

    while True:
        print("\nPilih Opsi Transformasi : ")
        print("1. Translasi")
        print("2. Scaling")
        print("3. Rotasi X")
        print("4. Rotasi Y")
        print("5. Rotasi Z")
        print("6. Shearing")
        print("7. Gabungan Transformasi")
        print("8. Undo Transformasi Terakhir")
        print("9. Reset Ke Bentuk Awal")
        print("10. Tampilkan Wireframe")
        print("11. Keluar")

        choice = int(input("Masukkan pilihan (1-11) : "))

        if choice == 1:
            dx, dy, dz = map(float, input("Masukkan dx dy dz: ").split())
            new_vertices = translate(vertices, dx, dy, dz)
            animate_transformation(vertices, new_vertices, edges)
            history.append(vertices)
            vertices = new_vertices

        elif choice == 2:
            sx, sy, sz = map(float, input("Masukkan sx sy sz: ").split())
            new_vertices = scale(vertices, sx, sy, sz)
            animate_transformation(vertices, new_vertices, edges)
            history.append(vertices)
            vertices = new_vertices

        elif choice == 3:
            angle = float(input("Masukkan sudut rotasi X: "))
            new_vertices = rotate_x(vertices, angle)
            animate_transformation(vertices, new_vertices, edges)
            history.append(vertices)
            vertices = new_vertices

        elif choice == 4:
            angle = float(input("Masukkan sudut rotasi Y: "))
            new_vertices = rotate_y(vertices, angle)
            animate_transformation(vertices, new_vertices, edges)
            history.append(vertices)
            vertices = new_vertices

        elif choice == 5:
            angle = float(input("Masukkan sudut rotasi Z: "))
            new_vertices = rotate_z(vertices, angle)
            animate_transformation(vertices, new_vertices, edges)
            history.append(vertices)
            vertices = new_vertices

        elif choice == 6:
            shx, shy = map(float, input("Masukkan shx shy: ").split())
            new_vertices = shear(vertices, shx, shy)
            history.append(vertices)
            vertices = new_vertices
            plot_wireframe(vertices, edges)

        elif choice == 7:
            n = int(input("Berapa banyak transformasi berturut-turut? "))
            history.append(vertices)
            for _ in range(n):
                sub_choice = int(input("Transformasi ke-{} (1: Translasi, 2: Skala, 3: RX, 4: RY, 5: RZ, 6: Shear): ".format(_+1)))
                if sub_choice == 1:
                    dx, dy, dz = map(float, input("  Masukkan dx dy dz: ").split())
                    vertices = translate(vertices, dx, dy, dz)
                elif sub_choice == 2:
                    sx, sy, sz = map(float, input("  Masukkan sx sy sz: ").split())
                    vertices = scale(vertices, sx, sy, sz)
                elif sub_choice == 3:
                    angle = float(input("  Masukkan sudut RX: "))
                    vertices = rotate_x(vertices, angle)
                elif sub_choice == 4:
                    angle = float(input("  Masukkan sudut RY: "))
                    vertices = rotate_y(vertices, angle)
                elif sub_choice == 5:
                    angle = float(input("  Masukkan sudut RZ: "))
                    vertices = rotate_z(vertices, angle)
                elif sub_choice == 6:
                    shx, shy = map(float, input("  Masukkan shx shy: ").split())
                    vertices = shear(vertices, shx, shy)
            plot_wireframe(vertices, edges)

        elif choice == 8:
            if history:
                vertices = history.pop()
                print("Transformasi terakhir dibatalkan.")
                plot_wireframe(vertices, edges)
            else:
                print("Tidak ada transformasi untuk di-undo.")

        elif choice == 9:
            vertices = original_vertices.copy()
            history.clear()
            print("Reset ke bentuk awal.")
            plot_wireframe(vertices, edges)

        elif choice == 10:
            plot_wireframe(vertices, edges)

        elif choice == 11:
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
