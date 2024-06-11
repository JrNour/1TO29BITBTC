from bit import Key

def convert_to_compressed_address(private_key):
    try:
        key = Key.from_hex(private_key)
        compressed_address = key.address
        return compressed_address
    except Exception as e:
        print(f"Error converting private key to compressed address: {e}")
        return None

def convert_private_keys(input_file, output_file):
    try:
        with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
            line_count = 0
            for line in f_in:
                private_key = line.strip()
                if not private_key:
                    continue
                compressed_address = convert_to_compressed_address(private_key)
                if compressed_address:
                    f_out.write(compressed_address + "\n")
                line_count += 1
                if line_count % 500000 == 0:
                    print(f"Processed {line_count} keys")
    except Exception as e:
        print(f"Error processing files: {e}")

if __name__ == "__main__":
    input_file = "lahex.txt"   # Input text file containing Bitcoin private keys
    output_file = "laadd.txt"  # Output text file to write compressed addresses
    
    print(f"Starting conversion from {input_file} to {output_file}")
    convert_private_keys(input_file, output_file)
    print("Compressed addresses generated and written ")
