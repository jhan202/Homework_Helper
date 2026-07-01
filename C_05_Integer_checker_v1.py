def int_check(question, low, high):
    """Checks user enters a number between two values ( allows decimals)"""

    error = f"Oops - please enter a number between {low} and {high}."

    while True:
        try:
            response = float(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



