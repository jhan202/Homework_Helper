def num_check(question, num_type="float", exit_code=""):
    """Checks user enters a valid number or allows enter for infinity mode"""

    while True:
        response = input(question)

        # Enter pressed = infinity mode trigger
        if exit_code is not None and response == exit_code:
            return response

        try:
            # convert to correct type
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            # only accept positive numbers
            if response > 0:
                return response
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")






