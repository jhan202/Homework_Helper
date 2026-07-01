import math


# Functions go here

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
For each problem enter:
- The shape you want to calculate
- The required dimensions

The program will calculate the surface area and volume.

Enter 'xxx' to exit infinity mode.
    ''')


def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


def string_check(question, valid_ans_list, num_letters):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def int_check(question, low, high):
    """Checks users enter an integer between two values."""

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


def num_check(question, num_type="float", exit_code=None):
    """Checks users enter an integer / float that is more than
    zero (or the optional exit code)"""

    while True:
        response = input(question)

        # check for exit code and return it if entered
        if exit_code is not None and response == exit_code:
            return response

        try:
            # change to correct number type
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            # check number is more than zero
            if response > 0:
                return response
            else:
                print("Oops - please enter a number more than 0.")

        except ValueError:
            print("Oops - please enter a valid number.")


def shape_calc(shape):
    """Calculates and prints the surface area and volume for the chosen shape.
    Returns (dimensions string, surface area, volume)"""

    if shape == "cube":
        side = int_check("Enter side length: ", 1, 100)
        surface_area = 6 * side * side
        volume = side ** 3
        print(f"Surface Area: {surface_area} cm^2")
        print(f"Volume: {volume} cm^3")
        dimensions = f"side: {side}"

    elif shape == "cuboid":
        length = int_check("Enter length: ", 1, 100)
        width = int_check("Enter width: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        surface_area = 2 * (length * width + length * height + width * height)
        volume = length * width * height
        print(f"Surface Area: {surface_area} cm^2")
        print(f"Volume: {volume} cm^3")
        dimensions = f"l:{length} w:{width} h:{height}"

    elif shape == "cylinder":
        radius = int_check("Enter radius: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        surface_area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
        volume = math.pi * radius ** 2 * height
        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")
        dimensions = f"r:{radius} h:{height}"

    elif shape == "cone":
        radius = int_check("Enter radius: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        slant = math.sqrt(radius ** 2 + height ** 2)
        surface_area = math.pi * radius * (radius + slant)
        volume = (1 / 3) * math.pi * radius ** 2 * height
        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")
        dimensions = f"r:{radius} h:{height}"

    elif shape == "sphere":
        radius = int_check("Enter radius: ", 1, 100)
        surface_area = 4 * math.pi * radius ** 2
        volume = (4 / 3) * math.pi * radius ** 3
        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")
        dimensions = f"radius: {radius}"

    return dimensions, round(surface_area, 2), round(volume, 2)


# Main routine goes here

# shape options
shape_list = ['cube', 'cuboid', 'cylinder', 'cone', 'sphere']

# result lists
all_shapes = []
all_dimensions = []
all_surface_areas = []
all_volumes = []

make_statement("Surface Area and Volume Calculator", "=")
print()

# ask if user wants instructions
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# ask how many problems - press enter for infinity mode
num_problems = num_check("How many problems do you want to solve? "
                         "(press enter for infinity mode): ",
                         "integer", "")

# check for infinity mode
if num_problems == "":
    infinity_mode = True
    problems_solved = 0
    print("Infinity mode activated! Enter 'xxx' to exit.\n")
else:
    infinity_mode = False
    problems_solved = 0

# Main problem loop
while True:

    # check if we have solved all problems (non-infinity mode)
    if not infinity_mode and problems_solved >= num_problems:
        break

    problems_solved += 1

    # show problem number
    if infinity_mode:
        make_statement(f"Problem {problems_solved}", "-")
    else:
        make_statement(f"Problem {problems_solved} of {num_problems}", "-")

    print()

    # choose a shape (xxx to exit)
    shape = string_check("Choose a shape (cube / cuboid / cylinder / cone / sphere)"
                         " or 'xxx' to exit: ",
                         shape_list + ['xxx'], 2)

    # exit code check
    if shape == "xxx":
        problems_solved -= 1
        print("See ya!!.\n")
        break

    print(f"You chose: {shape}")
    print()

    # calculate and store results
    dimensions, surface_area, volume = shape_calc(shape)

    all_shapes.append(shape)
    all_dimensions.append(dimensions)
    all_surface_areas.append(surface_area)
    all_volumes.append(volume)

    print()

# show how many problems were solved
print()
if infinity_mode:
    make_statement(f"You solved {len(all_shapes)} problems", "-")
else:
    make_statement(f"You solved {len(all_shapes)} / {num_problems} problems", "-")