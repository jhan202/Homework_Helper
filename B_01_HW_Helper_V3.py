from tabulate import tabulate  # nice clean table output instead of print statements everywhere
from datetime import date
import math


def make_statement(statement, decoration):
    # just a little header printer so things don't look like a wall of text
    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("Instructions", "ℹ️")
    # multi-line string is easier to read/edit than a bunch of separate print() calls
    print("""
For each problem enter:
- The shape you want to calculate (cube, cuboid, cylinder, cone, sphere)
- The required dimensions for that shape

The program will then calculate:
- Surface Area
- Volume

You can:
- Press ENTER to enable infinity mode (unlimited problems)
- Type 'xxx' at any time during shape selection to exit early
    """)


def string_check(question, valid_ans_list, num_letters):
    # keeps asking until the user gives something valid - either the full
    # word or a short version of it, e.g. typing "cyl" instead of "cylinder"
    while True:
        response = input(question).strip().lower()

        for item in valid_ans_list:
            if response == item:
                return item

            # startswith lets people type any length abbreviation, not just
            # one fixed length - "cub" and "cubo" both work for cuboid now
            elif len(response) >= num_letters and item.startswith(response):
                return item

        print(f"Invalid input. Choose from {valid_ans_list}")


def num_check(question, num_type="float", exit_code=None):
    # one function handles both float and integer input so, I'm not
    # duplicating this validation loop everywhere I need a number
    while True:
        response = input(question).strip()

        # exit_code lets this double as the infinity-mode trigger - pressing
        # enter with no number sends an empty string through here
        if exit_code is not None and response == exit_code:
            return response

        try:
            if num_type == "float":
                response = float(response)
                if response >= 0.1:
                    return response
                print("Number must be at least 0.1")

            elif num_type == "integer":
                # convert to float first so something like "3.5" gets
                # caught here instead of crashing when I force it to int
                response = float(response)
                if response != int(response):
                    print("Please enter a whole number only.")
                    continue

                response = int(response)
                if response > 0:
                    return response
                print("Number must be greater than 0")

        except ValueError:
            print("Invalid number - try again")


#  shape formulas
# each one grabs its own dimensions, does the maths, and hands back a
# string for the table plus the raw surface area / volume numbers

def cube():
    side = num_check("Enter side length: ", "float")
    sa = 6 * side * side
    vol = side ** 3
    return f"side: {side}", sa, vol


def cuboid():
    l = num_check("Enter length: ", "float")
    w = num_check("Enter width: ", "float")
    h = num_check("Enter height: ", "float")
    sa = 2 * (l * w + l * h + w * h)
    vol = l * w * h
    return f"l:{l} w:{w} h:{h}", sa, vol


def cylinder():
    r = num_check("Enter radius: ", "float")
    h = num_check("Enter height: ", "float")
    sa = 2 * math.pi * r ** 2 + 2 * math.pi * r * h  # two circle ends + the curved side
    vol = math.pi * r ** 2 * h
    return f"r:{r} h:{h}", sa, vol


def cone():
    r = num_check("Enter radius: ", "float")
    h = num_check("Enter height: ", "float")
    slant = math.sqrt(r ** 2 + h ** 2)  # pythagoras - need this for the curved surface area
    sa = math.pi * r * (r + slant)
    vol = (1 / 3) * math.pi * r ** 2 * h
    return f"r:{r} h:{h}", sa, vol


def sphere():
    r = num_check("Enter radius: ", "float")
    sa = 4 * math.pi * r ** 2
    vol = (4 / 3) * math.pi * r ** 3
    return f"radius: {r}", sa, vol


# dictionary means shape_calc can just look the function up by name instead
# of a massive if/elif chain - also makes it way easier to add a new shape later
shape_functions = {
    "cube": cube,
    "cuboid": cuboid,
    "cylinder": cylinder,
    "cone": cone,
    "sphere": sphere
}


def shape_calc(shape):
    dimensions, surface_area, volume = shape_functions[shape]()

    # round first so the printed output and the table always show the same value
    surface_area = round(surface_area, 2)
    volume = round(volume, 2)

    print(f"Surface Area: {surface_area}")
    print(f"Volume: {volume}")

    return dimensions, surface_area, volume


def results_table(all_shapes, all_dimensions, all_surface_areas, all_volumes):
    # zip stitches the four parallel lists back together row by row
    data = list(zip(all_shapes, all_dimensions, all_surface_areas, all_volumes))
    headers = ["Shape", "Dimensions", "Surface Area (cm^2)", "Volume (cm^3)"]
    return tabulate(data, headers=headers, tablefmt="psql")


def write_to_file(results):
    file_name = "shape_results.txt"

    with open(file_name, "w") as text_file:
        text_file.write("Surface Area and Volume Calculator Results\n")
        text_file.write(f"Date: {date.today()}\n\n")
        text_file.write(results)

    print(f"Saved successfully to {file_name}")


shape_list = list(shape_functions.keys())

# these four lists grow together, one entry per problem solved
all_shapes = []
all_dimensions = []
all_surface_areas = []
all_volumes = []

make_statement("Surface Area and Volume Calculator", "=")
print()

want_instructions = string_check("Do you want instructions? (yes/no): ", ["yes", "no"], 1)
if want_instructions == "yes":
    instructions()

print()

# empty string here = infinity mode, handled below
num_problems = num_check("How many problems? (press enter for infinity mode): ", "integer", "")

if num_problems == "":
    infinity_mode = True
    problems_solved = 0
    print("Infinity mode ON - type 'xxx' to exit anytime\n")
else:
    infinity_mode = False
    problems_solved = 0


# main loop - keeps going until the user hits their problem limit or types 'xxx' to bail out early
while True:

    # if the user picked a set number of problems ,and we've hit it, stop here
    if not infinity_mode and problems_solved >= num_problems:
        break

    problems_solved += 1

    # header for each problem - infinite mode just counts up freely,
    # regular mode shows progress like "Problem 2 of 5" so the user knows where they're at
    if infinity_mode:
        make_statement(f"Problem {problems_solved}", "-")
    else:
        make_statement(f"Problem {problems_solved} of {num_problems}", "-")

    print()

    # ask the user which shape they want - accepts full words or short versions
    shape = string_check(
        "Shape (cub=cube / cubo=cuboid / cyl=cylinder / con=cone / sph=sphere / xxx to exit): ",
        ['cube', 'cuboid', 'cylinder', 'cone', 'sphere', 'xxx'],
        3
    )

    # 'xxx' is the escape hatch - works at any point during shape selection
    if shape == "xxx":
        problems_solved -= 1  # this one didn't actually count, so undo the increment
        print("Exiting...\n")
        break

    print(f"You chose: {shape}\n")

    # run the right formula and get back the dimensions string + rounded SA and volume
    dimensions, surface_area, volume = shape_calc(shape)

    # add this problem's results to each list so they all stay in sync for the final table
    all_shapes.append(shape)
    all_dimensions.append(dimensions)
    all_surface_areas.append(surface_area)
    all_volumes.append(volume)

    print()


print()

# summary line - wording changes depending on whether they used infinity mode or not
if infinity_mode:
    make_statement(f"You solved {len(all_shapes)} problems", "-")
else:
    # len(all_shapes) is used instead of problems_solved in case they exited early with 'xxx'
    make_statement(f"You solved {len(all_shapes)} / {num_problems} problems", "-")

print()

# build and print the final results table using all the stored lists! :)
results = results_table(all_shapes, all_dimensions, all_surface_areas, all_volumes)
print(results)

print()

# give the user the option to save everything to a text file before the program closes
save_results = string_check("Save results? (yes/no): ", ["yes", "no"], 1)
if save_results == "yes":
    write_to_file(results)
    