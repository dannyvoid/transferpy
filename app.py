import os, subprocess, shutil, time, pathlib

filetypes = {
    "audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"],
    "images": [".jpg", ".jpeg", ".png", ".bpm", ".tiff", ".webp"],
    "text": [".txt", ".doc", ".docx", ".pdf", ".rtf", ".xls", ".xlsx"],
    "misc": [".heic", ".psd", ".torrent"],
    "videos": [
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
}


def move_file(file, destination_dir):
    file = os.path.normpath(file)
    destination_dir = os.path.normpath(destination_dir)
    try:
        shutil.move(file, destination_dir)
        message = f"Moved file: {file} to {destination_dir}"
    except Exception as e:
        message = f"Error: {e}"
    finally:
        print(message)


def valid_filetypes(extension):
    for key, value in filetypes.items():
        if extension in value:
            return True
    return False


def loose_files(directory):
    loose_files = next(os.walk(directory))[2]
    if loose_files:
        return loose_files
    return False


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print("closing in", timer, "seconds", end="\r")
        time.sleep(1)
        t -= 1


def remove_empty_folders(path):
    walk = list(os.walk(path))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            shutil.rmtree(path)


def main():
    while True:
        input_directory = input("Enter input directory: ")
        input_directory = pathlib.Path(input_directory)

        destination_directory = input("Enter destination directory: ")
        destination_directory = pathlib.Path(destination_directory)

        if input_directory.exists() and destination_directory.exists():
            for file in input_directory.rglob("*"):
                if file.is_file():
                    if valid_filetypes(file.suffix):
                        move_file(file, destination_directory)
        else:
            print("Invalid directory")
            continue

        if not loose_files(input_directory):
            if input("Delete input directory? (y/n): ").lower() == "y":
                shutil.rmtree(input_directory)
        else:
            print("There are loose files in the input directory")
        if input("Open destination directory? (y/n): ").lower() == "y":
            subprocess.Popen(r'explorer /select,"{}"'.format(destination_directory))
        if input("Close program? (y/n): ").lower() == "y":
            break
        else:
            continue


if __name__ == "__main__":
    main()
    countdown(5)
