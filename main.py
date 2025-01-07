import os
import hashlib

def calculate_file_hash(filepath, algorithm="sha256"):
    """Calculate the hash of a single file."""
    hash_func = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def process_directory(directory, output_file, algorithm="sha256"):
    """Walk through the directory, calculate file hashes, and save them to a file."""
    # Get the absolute paths of files to ignore
    ignored_files = {os.path.abspath(output_file), os.path.abspath(__file__)}
    
    with open(output_file, "w") as f:
        for root, _, files in os.walk(directory):
            for file in files:
                filepath = os.path.abspath(os.path.join(root, file))
                if filepath in ignored_files:
                    continue  # Skip ignored files
                try:
                    print(f"Calculating hash for {filepath}")
                    file_hash = calculate_file_hash(filepath, algorithm)
                    relative_path = os.path.relpath(filepath, directory)
                    f.write(f"{file_hash}  {relative_path}\n")
                except Exception as e:
                    print(f"Error hashing file {filepath}: {e}")

def main():
    # Root directory to hash
    root_directory = input("Enter the directory to process: ").strip()
    # Output file for hashes
    hash_file = os.path.join(root_directory, "directory_hashes.txt")

    print(f"Calculating hashes for files in: {root_directory}")
    process_directory(root_directory, hash_file)

    # Calculate hash of the resulting txt file
    directory_hash = calculate_file_hash(hash_file)
    print(f"Hashes written to: {hash_file}")
    print(f"Hash of the hash file ({hash_file}): {directory_hash}")

if __name__ == "__main__":
    main()
