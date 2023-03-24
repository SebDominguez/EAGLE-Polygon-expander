from shapely.geometry import Polygon
from shapely.ops import unary_union
import sys

input_str = sys.argv[1]
global_scale_factor = float(sys.argv[2])

# Split the input string into words
words = input_str.split()

# Split the input string into words
words = input_str.split()

# Extract the polygon name and index
polygon_name = words[0]
global_polygon_width = int(words[1])

# Extract the coordinates
global_coordinates = []
for i in range(2, len(words)):
	if words[i] == ')':
		# End of coordinate tuple
		continue
	elif words[i][0] == '(':
		# Start of coordinate tuple
		x, y = words[i][1:], words[i+1][:-1]
		global_coordinates.append((float(x), float(y)))

# print(f"Polygon name: {polygon_name}")
# print(f"Polygon index: {global_polygon_width}")
# print(f"Coordinates: {global_coordinates}")
# print(f"Scale factor: {global_scale_factor}")

def expand_polygon(p,n):
	# Define a polygon
	polygon = Polygon(p)

	# Define the amount of expansion
	expansion_distance = n

	expanded_polygon = polygon.buffer(expansion_distance, join_style=2, cap_style=2)

	return expanded_polygon

def main():
	global global_coordinates
	global global_scale_factor
	global global_polygon_width
	result = expand_polygon(global_coordinates, global_scale_factor)
	formated = " ".join([f"({round(x, 5)} {round(y, 5)})" for x, y in result.exterior.coords])
	# Format the polygon string
	polygon_str = f"Polygon {global_polygon_width} {formated}"
	print(polygon_str)

if __name__ == "__main__":
	main()