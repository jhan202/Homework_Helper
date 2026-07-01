import math

def yes_no_check(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")


def choose_shape():
    shapes = ["cube", "cuboid", "cylinder", "cone", "sphere"] # shapes users can choose from
    while True:
        choice = input("Choose shape (cube,cuboid,cylinder,cone,sphere): ").lower()
        if choice in shapes:
            return choice
        else:
            print("Invalid shape, Try again!") # if users choose a shape that is not a part of the list output this


def int_check(question, low, high):
    error = f"Oops - please enter an integer between {low} and {high}."

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def shape_calc(shape):

    if shape == "cube":
        side = int_check("Enter side length: ", 1, 100)
        surface_area = 6 * side * side
        volume = side ** 3
        print(f"Surface Area: {surface_area} cm^2")
        print(f"Volume: {volume} cm^3")

    elif shape == "cuboid":
        length = int_check("Enter length: ", 1, 100)
        width = int_check("Enter width: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        surface_area = 2 * (length*width + length*height + width*height)
        volume = length * width * height
        print(f"Surface Area: {surface_area} cm^2")
        print(f"Volume: {volume} cm^3")

    elif shape == "cylinder":
        radius = int_check("Enter radius: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
        volume = math.pi * radius**2 * height
        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")

    elif shape == "cone":
        radius = int_check("Enter radius: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        slant = math.sqrt(radius**2 + height**2)
        surface_area = math.pi * radius * (radius + slant)
        volume = (1/3) * math.pi * radius**2 * height
        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")

    elif shape == "sphere":
        radius = int_check("Enter radius: ", 1, 100)
        surface_area = 4 * math.pi * radius**2
        volume = (4/3) * math.pi * radius**3
        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")

# main for beginning

while True:
    calculate = yes_no_check("\nDo you want to calculate surface area? (yes/no): ")

    if calculate == "no":
        print("See ya! :)")
        break

    shape = choose_shape()
    print(f"You chose: {shape}")

    shape_calc(shape)
