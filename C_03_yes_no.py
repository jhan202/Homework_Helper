# Functions go here
def string_check(question):

    valid_shapes = {
        "cube": ["cube", "cu"],
        "cuboid": ["cuboid", "cubo"],
        "cone": ["cone", "co"],
        "sphere": ["sphere", "sp"],
        "cylinder": ["cylinder", "cy"]
    }

    while True:
        response = input(question).lower()

        for shape, valid_inputs in valid_shapes.items():
            if response in valid_inputs:
                return shape

        print("Please choose cube, cuboid, cone, sphere, or cylinder")


# Main routine goes here
while True:
    shape_type = string_check("What shape: ")
    print(f"You chose {shape_type}")



