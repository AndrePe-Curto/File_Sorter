# File Organizer

This script organizes files in the current directory into folders based on their file extensions, excluding itself from being moved.

## Usage

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/file-organizer.git
    cd file-organizer
    ```

2. **Run the script:**

    ```sh
    python file_organizer.py
    ```

    The script will create directories for each unique file extension found in the current directory and move the respective files into these directories. The script itself (`file_organizer.py` or the compiled `.exe` file) will not be moved.

## How It Works

- The script identifies all files in the current directory and extracts their file extensions.
- It creates separate folders (`extension Files`) for each unique file extension.
- Files are then moved into their respective folders based on their extensions, excluding the script file (`file_organizer.py` or `.exe`) from being moved.

## Requirements

- Python 3.x
- `os` and `shutil` standard libraries

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Troubleshooting

If you encounter issues, ensure:
- The script is executed in a directory where files are intended to be organized.
- Python and required libraries are installed correctly.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository.

---

Feel free to customize the sections further based on additional details or features of your script. This README.md provides a basic structure to introduce users to your file organizer script on GitHub.
