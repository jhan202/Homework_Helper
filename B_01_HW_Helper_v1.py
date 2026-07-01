import pandas
from tabulate import tabulate
import math


# Functions
def make_statement(statement, decoration):
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_options):
    while True:
        response = input(question).lower()

        if response in valid_options:
            return response
        else:
            print("Please choose a valid option.")



def shape_calc(shape):

    if shape == "cube":  # if the user chooses shapes out put these results :
        side = int_check("Enter side length: ", 1, 100) # asks user for the side length
        answer = 6 * side * side  # calculate side length using user input
        print(f"Answer: {answer} cm^2")  # Outputs results too user

    elif shape == "cuboid":
        length = int_check("Enter length: ", 1, 100)
        width = int_check("Enter width: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        answer = 2 * (length*width + length*height + width*height)
        print(f"Answer: {answer} cm^2")

    elif shape == "cylinder":
        radius = int_check("Enter radius: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        answer = 2 * 3.14 * radius**2 + 2 * 3.14 * radius * height
        print(f"Answer: {round(answer,2)} cm^2")

    elif shape == "cone":
        radius = int_check("Enter radius: ", 1, 100)
        height = int_check("Enter height: ", 1, 100)
        slant = (radius**2 + height**2) ** 0.5
        answer = 3.14 * radius * (radius + slant)
        print(f"Answer: {round(answer,2)} cm^2")

    elif shape == "sphere":
        radius = int_check("Enter radius: ", 1, 100)
        answer = 4 * 3.14 * radius**2
        print(f"Answer: {round(answer,2)} cm^2")

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

def panda_table(all_shapes, all_dimensions, all_surface_areas, all_volumes):

    results = {
        "Shape": all_shapes,
        "Dimensions": all_dimensions,
        "Surface Area": all_surface_areas,
        "Volume": all_volumes
    }

    results_frame = pandas.DataFrame(results)

    # round values
    results_frame["Surface Area"] = results_frame["Surface Area"].round(2)
    results_frame["Volume"] = results_frame["Volume"].round(2)

    table = tabulate(results_frame, headers='keys', tablefmt='psql', showindex=False)

    print(table)


# Main program
make_statement("Surface Area and Volume Calculator", "=")

all_shapes = []
all_dimensions = []
all_surface_areas = []
all_volumes = []


# ask how many problems (boundary testing)
while True:
    try:
        number_of_problems = int(input("How many problems do you want to solve (1-10): "))

        if 1 <= number_of_problems <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")

    except ValueError:
        print("Please enter a whole number.")


# loop through problems
for i in range(number_of_problems):

    print(f"\nProblem {i + 1}")

    shape = string_check(
        "Choose a shape (cube / cuboid / sphere): ",
        ["cube", "cuboid", "sphere"]
    )

