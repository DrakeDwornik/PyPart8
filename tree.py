import os
import logging
import sys

def file_write(file, contents):
    file.write(contents)

def create_directory_tree(directory: str = ".", filename: str = "output_file.txt"):
    file = None
    try:
        file = open(filename, "w")
    except OSError as err:
        print("OS error opening the file, please make sure you have permission to write")
        logging.error(err)
    else:
        contents = file_tree(directory)
        file_write(file,contents)
    finally:
        file.close() if file else logging.warning("No file resource available to close.")


def file_tree(input_path: str = '.', output_file: str = "output.txt"):
    file_tree = ""
    for dirpath, dirnames, filenames in os.walk(input_path):
        for filename in filenames:
            file_tree += f"{dirpath}/{filename}\n"
    return file_tree

if __name__ == '__main__':
    create_directory_tree(str(sys.argv[1]))
