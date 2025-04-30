def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied while accessing the file '{file_path}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred while reading the file: {e}")

def modify_content(content):
    return content.upper()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)