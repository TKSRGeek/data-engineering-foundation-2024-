import os

# 1. Get Current Working Directory
# print(os.getcwd())
#
# 2. Make Directory/Folder
# os.mkdir("movies")
#
# 3. Parent should be available then you'd be able to make another folder inside it.
# os.mkdir("movies/action")  # 👈 Folder inside Folder
#
# 4. In this case you don't need to have parent, it will create it for you.
# os.makedirs("games/adventure")
#
# 5. Change directory
# print(os.getcwd())
# os.chdir("games")
# print(os.getcwd())
#
# 6. Rename Directory
# os.rename("games", "tiktoks")
#
# 7. Remove Directory
# os.rmdir("tiktoks")  # Folder should be empty, then you can delete it.
# os.rmdir("games/adventure")  # Remove Child Folder

# 8. Remove All
os.removedirs("movies/action")


#
# Example: File and Folder Handling
# Creating a Directory
# Creating Files
# Reading Files
# Deleting Files
# import os

def create_directory(directory_name):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

def create_file(directory, file_name, content=""):
    """Create a file with given content."""
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' created with content.")

def read_file(directory, file_name):
    """Read and return the content of a file."""
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Content of '{file_path}':\n{content}")
        return content
    else:
        print(f"File '{file_path}' does not exist.")
        return None

def delete_file(directory, file_name):
    """Delete a specified file."""
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

def file_folder_operations(operation, *args, **kwargs):
    """Handle file and folder operations."""
    if operation == "create_directory":
        create_directory(*args, **kwargs)
    elif operation == "create_file":
        create_file(*args, **kwargs)
    elif operation == "read_file":
        return read_file(*args, **kwargs)
    elif operation == "delete_file":
        delete_file(*args, **kwargs)
    else:
        print("Invalid operation.")

# Example usage
file_folder_operations("create_directory", "test_directory")
file_folder_operations("create_file", "test_directory", "test_file.txt", content="Hello, World!")
content = file_folder_operations("read_file", "test_directory", "test_file.txt")
file_folder_operations("delete_file", "test_directory", "test_file.txt")
