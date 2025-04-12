from transformations import translate, scale, rotate_x, rotate_y, rotate_z, shear
from wireframe import create_cube, plot_wireframe

def main():
    vertices, edges = create_cube()
    
    print("Pilih Transformasi:")
    print("1. Translasi")
    print("2. Scaling")
    print("3. Rotasi X")
    print("4. Rotasi Y")
    print("5. Rotasi Z")
    print("6. Shearing")
    
    choice = int(input("Masukkan pilihan (1-6): "))

    if choice == 1:
        dx, dy, dz = map(float, input("Masukkan dx dy dz: ").split())
        vertices = translate(vertices, dx, dy, dz)
    elif choice == 2:
        sx, sy, sz = map(float, input("Masukkan sx sy sz: ").split())
        vertices = scale(vertices, sx, sy, sz)
    elif choice == 3:
        angle = float(input("Masukkan sudut rotasi X: "))
        vertices = rotate_x(vertices, angle)
    elif choice == 4:
        angle = float(input("Masukkan sudut rotasi Y: "))
        vertices = rotate_y(vertices, angle)
    elif choice == 5:
        angle = float(input("Masukkan sudut rotasi Z: "))
        vertices = rotate_z(vertices, angle)
    elif choice == 6:
        shx, shy = map(float, input("Masukkan shx shy: ").split())
        vertices = shear(vertices, shx, shy)
    
    plot_wireframe(vertices, edges)

if __name__ == "__main__":
    main()
