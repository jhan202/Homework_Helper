# Functions go here
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


# Main routine goes here

# testing num_check
my_float = num_check("Enter a number more than 0: ")
print(f"You entered {my_float}")

my_int = num_check("Enter an integer more than 0: ", "integer")
print(f"You entered {my_int}")

