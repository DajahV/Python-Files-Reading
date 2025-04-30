import os
from file_operations import read_file, modify_content, write_file

def main():
    # Ask the user for a filename
    input_file = input("Enter the name of the text file to modify (with extension): ")

    # Check if the file exists and handle errors
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    try:
        # Read the content of the input file
        content = read_file(input_file)

        # Modify the content
        modified_content = modify_content(content)

        # Generate output file name
        output_file = f"modified_{input_file}"

        # Write the modified content to the output file
        write_file(output_file, modified_content)

        print(f"Modified content written to {output_file}")
    except PermissionError:
        print(f"Error: Permission denied while accessing the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()