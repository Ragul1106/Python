import logging

logging.basicConfig(filename='filereader.log', level=logging.ERROR)

def read_file_secure(filename):
    file = None
    try:
        try:
            file = open(filename, 'r')
            content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist")
        except PermissionError:
            raise PermissionError("No permission to read file")
        else:
            print("File content:")
            print(content)
    except Exception as e:
        logging.error(f"File error: {e}")
        print(f"Error: {e}")
    finally:
        if file is not None:
            file.close()
            print("File closed")

read_file_secure("example.txt")