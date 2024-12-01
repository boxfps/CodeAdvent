# The challenge boils down to being given 2 columns of data (seen in the .txt)
# that I need to sort in ascending order, and find the difference of the paired 
# numbers. I then have to add all of the differences together to get a total number

# reference my input file
input_file = "locations-part1.txt"

# create empty lists to read the data into
left_column = []
right_column = []

# read the data into the lists
with open(input_file, "r") as f:
    for line in f:
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            left_column.append(parts[0])
            right_column.append(parts[1])

# sort the lists in ascending numerical order
left_column.sort(key=int)
right_column.sort(key=int)

# create a list for the difference in each pair
differences = []
# ensure both columns are the same length
if len(left_column) == len(right_column): 
    for i in range(len(left_column)):
        left_value = int(left_column[i])
        right_value = int(right_column[i])
        # find the absolute difference, no neg numbers
        difference = abs(left_value - right_value) 
        differences.append(difference)
else:
    print("The columns do not have the same length!")

total = sum(differences)
print(total)