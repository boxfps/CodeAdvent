# Part 2 is similar to part 1, i am using the same two lists. 
# Although now I need to see how many times a number in the 
# left column appears in the right column. Then multiply them.

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
            left_column.append(int(parts[0]))
            right_column.append(int(parts[1]))

# Initialize total similarity score
total_similarity_score = 0

# Iterate over each number in the left column
for num in left_column:
    count = right_column.count(num)  # Count occurrences in the right column
    total_similarity_score += num * count  # Multiply and add to total score

# Output the result
print("Total Similarity Score:", total_similarity_score)