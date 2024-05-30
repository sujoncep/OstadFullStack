
def calculateArea(radius):
    pi = 3.14159
    return pi * radius ** 2


def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculateArea(radius)
    print(f"A = {area}")


if __name__ == "__main__":
    main()
