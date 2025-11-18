# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
#  forthis we use chatgpt as copy paste this ques.
import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)
        print(f"Contents of '{path}':")
        for name in entries:
            print(name)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to read '{path}'.")

if __name__ == "__main__":
    user_path = input("Enter directory path (leave blank for current directory): ").strip()
    if not user_path:
        user_path = "."  # current directory
    print_directory_contents(user_path)
