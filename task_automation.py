import os
import shutil

def organize_files():
    directory = input("Please enter the directory path to organize: ").strip()
    if not os.path.exists(directory):
        print("Directory not found! Please provide a valid path.")
        return

    extensions = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"],
    }

    for category, exts in extensions.items():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created/Checked folder: {folder_path}")

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                if any(file.endswith(ext) for ext in exts):
                    try:
                        shutil.move(file_path, folder_path)
                        print(f"Moved file: {file} -> {folder_path}")
                    except Exception as e:
                        print(f"Error moving file {file}: {e}")

    print("Files organized successfully!")

if __name__ == "__main__":
    organize_files()
