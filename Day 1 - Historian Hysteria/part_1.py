left = []
right = []
total_dist = 0

# Read the input file from Advent of Code
with open("input.txt", 'r') as file:
    contents = file.readlines()

    # For every line "1234    5678" break them up into
    # individual numbers (1234, 5678) and put them in their respective lists
    for line in contents:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

# Sort the lists so the partner numbers will have the same indices
left.sort()
right.sort()

assert len(left) == len(right)

# Start summing up the differences in the numbers
for i in range(len(left)):
    total_dist += abs(left[i] - right[i])

print(total_dist)
