# Directory Integrity Checker

This Python script calculates the hashes of all files in a directory and its subdirectories, excluding itself and the output hash file. It generates a `.txt` file containing these hashes and their relative paths. The resulting `.txt` file can then be used to verify the integrity of the directory.

## Features
- Recursively traverses a directory and its subdirectories.
- Calculates file hashes using the SHA-256 algorithm (default).
- Excludes the script file (`main.py`) and the output hash file (`directory_hashes.txt`) from calculations.
- Writes the hashes and relative file paths to a `.txt` file for easy verification.

## Requirements
- Python 3.8 or higher

## Installation
1. Clone the repository or download the script:
    git clone https://github.com/hiramzabdy/directoryHashCalculator.git
    cd directoryHashCalculator

2. Ensure you have Python installed
    python --version

## Usage
1. Place the script (`main.py`) inside the directory you want to hash.

2. Run the script:
    python main.py

3. Enter the path to the directory when prompted. For example:
    Enter the directory to process: .

4. The script will generate a file named directory_hashes.txt in the specified directory. It will also display the hash of this file.

## Example output
The directory_hashes.txt file will look like this:

    a3f1e1e5f6b9ec53d5d6eada55f8b1e4d43b43dc1c2f8e35e24c6a0e17c3bbd  folder1/file1.txt
    5b67c123b5eaf34e5a45d2b7c634e91e53f87b2e1d5f2c9a6a7f5c2a3b4c5d6  folder2/file3.txt

The hash of directory_hashes.txt itself will be displayed in the terminal.

## Use Cases
    Verify file integrity in backups.
    Detect changes in a directory over time.