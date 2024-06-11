def generate_and_write_sequential_hex(lower_bound, upper_bound, output_file):
    with open(output_file, 'w') as f:
        for num in range(lower_bound, upper_bound + 1):
            # Convert the number to hexadecimal format with leading zeros and 64 characters
            hex_number = '{:064x}'.format(num)
            f.write(hex_number + "\n")
            
            # Print progress for every 1,000,000 numbers
            if num % 1000000 == 0:
                print(f"Processed {num} numbers")

# Define the lower and upper bounds of the range
lower_bound = 0x10000000
upper_bound = 0x1fffffff  # Adjusted 

# Specify the output file
output_file = "29bithex.txt"

# Generate and write sequential hexadecimal numbers directly to the output file
generate_and_write_sequential_hex(lower_bound, upper_bound, output_file)

print(f"Generated sequential hexadecimal numbers have been written to {output_file}")
