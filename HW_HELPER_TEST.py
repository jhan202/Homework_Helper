print("✖️➕➗ HOMEWORK HELPERS ✖️➕➗")

def yes_no_check(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no.")

def make_statement(statement, decoration):
    print(f"{decoration*3} {statement} {decoration*3}")

def instructions():
    make_statement("INSTRUCTIONS", "❓")
    print("""
Welcome to HOMEWORK HELPERS
This program will help you calculate the surface area of 3D shapes.
You can choose from: cube, cuboid, cylinder, cone, sphere.
Follow the prompts and enter the requested dimensions.
You can solve multiple problems and save your results to a file.
""")

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def choose_shape():
    shapes = ["cube", "cuboid", "cylinder", "cone", "sphere"]
    while True:
        choice = input("Choose shape (cube,cuboid,cylinder ,cone, sphere): ").lower()
        if choice in shapes:
            return choice
        else:
            print("Invalid shape. Try again.")


# Ask if user wants instructions
want_instructions = yes_no_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()


    def num_check(question, num_type="float", exit_code=None):
        """Checks users enter an integer / float that is more than
        zero (or the optional exit code)"""

        while True:
            response = input(question)

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

def yes_no_check(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "You chose yes."
        elif response in ["no", "n"]:
            return "You chose no."
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

    if shape == "cube":  # if the user chooses shapes out put these results :
        side = int_check("Enter side length: ", 1, 100) # asks user for the side length
        answer = 6 * side * side  # calculate side length using user input
        print(f"Answer: {answer} cm^2")  # Outputs results too user

    elif shape == "cuboid":
        length = int_check("Enter length: ",1 , 100)
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


# main for beginning

while True:
    calculate = yes_no_check("\nDo you want to calculate surface area? (yes/no): ")

    if calculate == "no":
        print("See ya! :)")
        break

    shape = choose_shape()
    print(f"You chose: {shape}")

    shape_calc(shape)


