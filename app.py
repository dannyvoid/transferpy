import os
import shutil
import pathlib
import subprocess

file_types = [
    ("audio", [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"]),
    ("images", [".jpg", ".jpeg", ".png", ".bpm", ".tiff", ".webp"]),
    ("text", [".txt", ".doc", ".docx", ".pdf", ".rtf", ".xls", ".xlsx"]),
    ("misc", [".heic", ".psd", ".torrent"]),
    (
        "videos",
        [
            ".mp4",
            ".ts",
            ".mkv",
            ".avi",
            ".flv",
            ".wmv",
            ".mov",
            ".mpg",
            ".mpeg",
            ".m4v",
            ".webm",
            ".gif",
        ],
    ),
]


def copy_file(src, dst):
    src = pathlib.Path(src)
    dst = pathlib.Path(dst)
    shutil.copy2(src, dst)
    print(f"Copied file: {src} to {dst}")
    src.unlink()
    print(f"Removed file: {src}")


def get_file_type(extension):
    for file_type, extensions in file_types:
        if extension in extensions:
            return file_type
    return None


def main():
    while True:
        input_directory = input("Enter input directory: ")
        input_directory = pathlib.Path(input_directory)

        destination_directory = input("Enter destination directory: ")
        destination_directory = pathlib.Path(destination_directory)

        if not input_directory.exists() or not destination_directory.exists():
            print("Invalid directory")
            continue

        for file in input_directory.rglob("*"):
            if file.is_file():
                file_type = get_file_type(file.suffix)
                if file_type is not None:
                    destination_dir = destination_directory / file_type
                    if not destination_dir.exists():
                        os.makedirs(destination_dir)
                    copy_file(file, destination_dir)

        if not os.listdir(input_directory):
            if input("Delete input directory? (y/n): ").lower() == "y":
                shutil.rmtree(input_directory)
        else:
            print("There are loose files in the input directory")
        if input("Open destination directory? (y/n): ").lower() == "y":
            subprocess.run(["explorer.exe", "/select,", str(destination_directory)])
        if input("Close program? (y/n): ").lower() == "y":
            break
        else:
            continue


if __name__ == "__main__":
    main()
