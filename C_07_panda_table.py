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

# create dataframe from dictionary
results_frame = pandas.DataFrame(results_dict)

# format numbers to 2 decimal places
results_frame["Surface Area (cm^2)"] = results_frame["Surface Area (cm^2)"].apply(round_2dp)
results_frame["Volume (cm^3)"] = results_frame["Volume (cm^3)"].apply(round_2dp)

# print table using tabulate
results_string = tabulate(results_frame, headers='keys', tablefmt='psql', showindex=False)
print(results_string)

