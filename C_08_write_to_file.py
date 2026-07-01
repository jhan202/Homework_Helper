import pandas
from tabulate import tabulate

# function to format numbers to 2 decimal places
def round_2dp(x):
    return f"{x:.2f}"

# hardcoded test data (to test the table before connecting to real program)
all_shapes = ["cube", "cuboid", "sphere"]
all_dimensions = ["side: 5", "l:2 w:3 h:4", "radius: 6"]
all_surface_areas = [150, 52, 452.39]
all_volumes = [125, 24, 904.78]

# dictionary
results_dict = {
    "Shape": all_shapes,
    "Dimensions": all_dimensions,
    "Surface Area (cm^2)": all_surface_areas,
    "Volume (cm^3)": all_volumes
}

# create dataframe
results_frame = pandas.DataFrame(results_dict)

# format numbers to 2 decimal places (for display only)
results_frame["Surface Area (cm^2)"] = results_frame["Surface Area (cm^2)"].apply(round_2dp)
results_frame["Volume (cm^3)"] = results_frame["Volume (cm^3)"].apply(round_2dp)

# convert table using TABULATE (required for C_08)
results_string = tabulate(results_frame, headers="keys", tablefmt="psql", showindex=False)

# content to write
to_write = [
    "Surface Area & Volume Results",
    "",
    results_string
]

# print to console (optional)
for item in to_write:
    print(item)

# write to file (C_08 OUTPUT)
file_name = "HW_Helper_results.txt"

with open(file_name, "w") as text_file:
    for item in to_write:
        text_file.write(item + "\n")

print("\nFile successfully saved as HW_Helper_results.txt")


