while True:
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    if width == 99 or height == 99:
        break

    area = width * height
    print(f"Width: {width}, Height: {height}, Area: {area}")