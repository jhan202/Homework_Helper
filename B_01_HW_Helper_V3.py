import pandas  # used to store results neatly in a table (like Excel inside Python)
from tabulate import tabulate  # makes the table look clean when printed in terminal
from datetime import date  # lets us add today’s date to saved files
import math  # needed for pi, square roots, and powers in shape formulas


# functions

def make_statement(statement, decoration):
    """Just makes headings stand out so the output isn’t boring"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    """Explains how the program works so the user isn’t confused"""
    make_statement("Instructions", "ℹ️")

    print('''
For each problem enter:
- The shape you want to calculate
- The required dimensions

The program will calculate the surface area and volume.

Press enter if you want unlimited problems (infinity mode).

Type 'xxx' if you want to stop early.
    ''')


def yes_no(question):
    """Keeps asking until the user actually says yes or no"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes (y) or no (n).")  # stops invalid input


def string_check(question, valid_ans_list, num_letters):
    """Checks if the user typed a valid option (full word or shortcut)"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # did they type the full correct word?
            if response == item:
                return item

            # or just the first few letters of it?
            elif response == item[:num_letters]:
                return item

        print(f"That’s not valid. Please choose from: {valid_ans_list}")


def num_check(question, num_type="float", exit_code=None):
    """Makes sure the user enters a real number and not random text"""

    while True:
        response = input(question)

        # lets infinity mode setup skip out cleanly
        if exit_code is not None and response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)

                if response > 0:
                    return response  # valid number
                else:
                    print("Number must be greater than 0.")

            elif num_type == "integer":
                response = float(response)

                # checks if user entered a decimal when we want a whole number
                if response != int(response):
                    print("Please enter a whole number only.")
                    continue

                response = int(response)

                if response > 0:
                    return response
                else:
                    print("Number must be greater than 0.")

        except ValueError:
            print("That’s not a valid number. Try again.")


def shape_calc(shape):
    """Does all the maths depending on which shape the user picked"""

    if shape == "cube":
        side = num_check("Enter side length: ", "float")

        surface_area = 6 * side * side  # cube formula
        volume = side ** 3  # cube formula

        print(f"Surface Area: {surface_area} cm^2")
        print(f"Volume: {volume} cm^3")

        dimensions = f"side: {side}"


    elif shape == "cuboid":
        length = num_check("Enter length: ", "float")
        width = num_check("Enter width: ", "float")
        height = num_check("Enter height: ", "float")

        surface_area = 2 * (length * width + length * height + width * height)
        volume = length * width * height

        print(f"Surface Area: {surface_area} cm^2")
        print(f"Volume: {volume} cm^3")

        dimensions = f"l:{length} w:{width} h:{height}"


    elif shape == "cylinder":
        radius = num_check("Enter radius: ", "float")
        height = num_check("Enter height: ", "float")

        surface_area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
        volume = math.pi * radius ** 2 * height

        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")

        dimensions = f"r:{radius} h:{height}"


    elif shape == "cone":
        radius = num_check("Enter radius: ", "float")
        height = num_check("Enter height: ", "float")

        slant_height = math.sqrt(radius ** 2 + height ** 2)  # used for cone surface area

        surface_area = math.pi * radius * (radius + slant_height)
        volume = (1 / 3) * math.pi * radius ** 2 * height

        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")

        dimensions = f"r:{radius} h:{height}"


    elif shape == "sphere":
        radius = num_check("Enter radius: ", "float")

        surface_area = 4 * math.pi * radius ** 2
        volume = (4 / 3) * math.pi * radius ** 3

        print(f"Surface Area: {round(surface_area, 2)} cm^2")
        print(f"Volume: {round(volume, 2)} cm^3")

        dimensions = f"radius: {radius}"

    return dimensions, round(surface_area, 2), round(volume, 2)


def panda_table(all_shapes, all_dimensions, all_surface_areas, all_volumes):
    """Turns all collected results into a clean printable table"""

    results_dict = {
        "Shape": all_shapes,
        "Dimensions": all_dimensions,
        "Surface Area (cm^2)": all_surface_areas,
        "Volume (cm^3)": all_volumes
    }

    results_frame = pandas.DataFrame(results_dict)  # converts lists into a proper table

    # rounds numbers so everything looks neat and consistent
    results_frame["Surface Area (cm^2)"] = results_frame["Surface Area (cm^2)"].round(2)
    results_frame["Volume (cm^3)"] = results_frame["Volume (cm^3)"].round(2)

    # makes it look nice in the terminal
    return tabulate(results_frame, headers='keys', tablefmt='psql', showindex=False)


def write_to_file(results):
    """Saves results into a text file so the user doesn’t lose them"""

    file_name = "shape_results.txt"

    with open(file_name, "w") as text_file:
        text_file.write("Surface Area and Volume Calculator Results\n")
        text_file.write(f"Date: {date.today()}\n\n")
        text_file.write(results)

    print(f"Saved successfully to {file_name}")

#  MY MAIN PROGRAM :)

shape_list = ['cube', 'cuboid', 'cylinder', 'cone', 'sphere']

# these lists store everything the user calculates
all_shapes = []
all_dimensions = []
all_surface_areas = []
all_volumes = []

make_statement("Surface Area and Volume Calculator", "=")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# asks how many problems OR lets user go infinite
num_problems = num_check(
    "How many problems do you want to solve? (press enter for infinity mode): ",
    "integer",
    ""
)

# checks which mode the program should run in
if num_problems == "":
    infinity_mode = True
    problems_solved = 0
    print("Infinity mode on — type 'xxx' to stop anytime.\n")

else:
    infinity_mode = False
    problems_solved = 0


while True:

    if not infinity_mode and problems_solved >= num_problems:
        break

    problems_solved += 1

    # shows progress so user knows what problem they’re on
    if infinity_mode:
        make_statement(f"Problem {problems_solved}", "-")
    else:
        make_statement(f"Problem {problems_solved} of {num_problems}", "-")

    print()

    # lets user choose shape
    shape = string_check(
        "Choose a shape (cube / cuboid / cylinder / cone / sphere) or 'xxx' to exit: ",
        shape_list + ['xxx'],
        3
    )

    # exit option
    if shape == "xxx":
        problems_solved -= 1
        print("Exiting...\n")
        break

    print(f"You chose: {shape}")
    print()

    # runs calculations
    dimensions, surface_area, volume = shape_calc(shape)

    # stores results so we can make a table later
    all_shapes.append(shape)
    all_dimensions.append(dimensions)
    all_surface_areas.append(surface_area)
    all_volumes.append(volume)

    print()

print()

# final summary
if infinity_mode:
    make_statement(f"You solved {len(all_shapes)} problems", "-")
else:
    make_statement(f"You solved {len(all_shapes)} / {num_problems} problems", "-")

print()

# creates final results table
results_table = panda_table(all_shapes, all_dimensions, all_surface_areas, all_volumes)
print(results_table)
print()

# saves file if user wants
save_results = yes_no("Would you like to save your results to a file? ")

if save_results == "yes":
    write_to_file(results_table)


