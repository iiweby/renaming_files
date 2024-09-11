import os

def rename_files_in_directory(directory_path, words_to_remove):
    """
    Renames files in the specified directory by removing specified words from filenames.

    :param directory_path: Path to the directory containing files to rename
    :param words_to_remove: List of words to remove from filenames
    """
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"Directory not found: {directory_path}")
        return

    # List all files in the directory
    for filename in os.listdir(directory_path):
        # Skip directories
        if os.path.isdir(os.path.join(directory_path, filename)):
            continue

        # Construct new filename
        new_filename = filename
        for word in words_to_remove:
            new_filename = new_filename.replace(word, "")

        # Ensure the new filename is different from the old one
        if new_filename != filename:
            old_path = os.path.join(directory_path, filename)
            new_path = os.path.join(directory_path, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")

# Example usage
directory = "C:\\Users\\Weby\\Desktop\\Code\\scdl\\Home of House"
words = ["_"]  # Replace with words you want to remove
rename_files_in_directory(directory, words)
