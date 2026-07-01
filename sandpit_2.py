import pandas
from tabulate import tabulate
from datetime import date
import math


# Functions go here

def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
For each problem enter:
- The shape you want to calculate
- The required dimensions

The program will calculate the surface area and volume.

Press enter when asked how many problems to enter infinity mode.

Enter 'xxx' when choosing a shape to exit infinity mode.
    '''
          )


def yes_no(question):
    """Checks that users enter yes / y or no / n"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes (y) or no (n).\n")


def string_check(question, valid_ans_list, num_letters):
    """Checks users enter full word or shortened version"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # full word check
            if response == item:
                return item

            # first letters check
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def int_check(question, low, high):
    """Checks users enter an integer between two values"""

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
    """Checks users enter valid numbers more than zero"""

    while True:
        response = input(question)

        # exit code check
        if exit_code is not None and response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)

            else:
                response = int(response)

            if response > 0:
                return response

            else:
                print("Oops - please enter a number more than 0.")

        except ValueError:
            print("Oops - please enter a valid number.")


def shape_calc(shape):
    """Calculates surface area and volume"""

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

        slant_height = math.sqrt(radius ** 2 + height ** 2)

        surface_area = math.pi * radius * (radius + slant_height)
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


def panda_table(all_shapes, all_dimensions, all_surface_areas, all_volumes):
    """Creates results table"""

    results_dict = {
        "Shape": all_shapes,
        "Dimensions": all_dimensions,
        "Surface Area (cm^2)": all_surface_areas,
        "Volume (cm^3)": all_volumes
    }

    results_frame = pandas.DataFrame(results_dict)

    results_string = tabulate(
        results_frame,
        headers='keys',
        tablefmt='psql',
        showindex=False
    )

    return results_string


def write_to_file(results):
    """Writes results to text file"""

    file_name = "shape_results.txt"

    with open(file_name, "w") as text_file:
        text_file.write("Surface Area and Volume Calculator Results\n")
        text_file.write(f"Date: {date.today()}\n\n")
        text_file.write(results)

    print(f"Results have been saved to {file_name}")


# Main routine goes here

shape_list = ['cube', 'cuboid', 'cylinder', 'cone', 'sphere']

all_shapes = []
all_dimensions = []
all_surface_areas = []
all_volumes = []

make_statement("Surface Area and Volume Calculator", "✖️➕➖")
print()

want_instructions = yes_no(" Do you want to see the instructions❓ ")

if want_instructions == "yes":
    instructions()

print()

num_problems = num_check(
    "How many problems do you want to solve? "
    "(press enter for infinity mode): ",
    "integer",
    ""
)

if num_problems == "":
    infinity_mode = True
    problems_solved = 0
    print("Infinity mode activated! Enter 'xxx' to exit.\n")

else:
    infinity_mode = False
    problems_solved = 0


while True:

    if not infinity_mode and problems_solved >= num_problems:
        break

    problems_solved += 1

    if infinity_mode:
        make_statement(f"Problem {problems_solved}", "-")

    else:
        make_statement(f"Problem {problems_solved} of {num_problems}", "-")

    print()

    shape = string_check(
        "Choose a shape (cube / cuboid / cylinder / cone / sphere) "
        "or 'xxx' to exit: ",
        shape_list + ['xxx'],
        3
    )

    if shape == "xxx":
        problems_solved -= 1
        print("Exiting...\n")
        break

    print(f"You chose: {shape}")
    print()

    dimensions, surface_area, volume = shape_calc(shape)

    all_shapes.append(shape)
    all_dimensions.append(dimensions)
    all_surface_areas.append(surface_area)
    all_volumes.append(volume)

    print()


print()

if infinity_mode:
    make_statement(f"You solved {len(all_shapes)} problems", "-")

else:
    make_statement(f"You solved {len(all_shapes)} / {num_problems} problems", "-")


print()

results_table = panda_table(
    all_shapes,
    all_dimensions,
    all_surface_areas,
    all_volumes
)

print(results_table)
print()

save_results = yes_no("Would you like to save your results to a file? ")

if save_results == "yes":
    write_to_file(results_table)

