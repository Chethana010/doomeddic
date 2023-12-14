# Define the number of sides for each die
num_sides_die_a = 6
num_sides_die_b = 6

total_combinations = num_sides_die_a * num_sides_die_b

print("Total Combinations:", total_combinations)

# Create an empty matrix to store combinations
combinations_matrix = [[0 for _ in range(num_sides_die_b)] for _ in range(num_sides_die_a)]

# Loop through each element of the matrix
for i in range(num_sides_die_a):
    for j in range(num_sides_die_b):
        # Calculate the sum of the dice rolls for the current combination
        combinations_matrix[i][j] = i + j + 2

# Print the combinations matrix
print("Combinations Matrix:")
for row in combinations_matrix:
    print(row)
