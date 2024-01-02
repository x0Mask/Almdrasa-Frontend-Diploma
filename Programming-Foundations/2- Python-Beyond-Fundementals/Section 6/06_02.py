input_file = open("values.txt", "rt")
output_file = open("output.txt", "wt")

total_sum = 0

# Loop through each line in the input file and calculate the sum
for line in input_file:
    total_sum += int(line)
    print(line.rstrip(), file=output_file)

print("Sum: " + str(total_sum), file=output_file)

# Close the output file
output_file.close()

# Print a message indicating the end of the code
print("I am done")