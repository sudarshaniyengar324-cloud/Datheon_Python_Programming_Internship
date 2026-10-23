import os
import shutil
from pathlib import Path

# Map file extensions to category folders
FILE_CATEGORIES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
}


def get_category(file_path):
    """Return the category for a file based on its extension."""
    return FILE_CATEGORIES.get(file_path.suffix.lower(), "Other")


def get_unique_destination(destination):
    """Choose a non-conflicting filename without overwriting files."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1


def organize_directory(directory, dry_run=False):
    """Organize files in the selected directory's top level."""
    source = Path(directory).expanduser()

    if not source.exists() or not source.is_dir():
        raise ValueError("The path must be an existing directory.")

    moved = 0
    skipped = 0
    failed = 0

    with os.scandir(source) as entries:
        for entry in entries:
            try:
                if not entry.is_file(follow_symlinks=False):
                    skipped += 1
                    continue

                file_path = Path(entry.path)

                if file_path.resolve() == Path(__file__).resolve():
                    skipped += 1
                    continue

                category = get_category(file_path)
                target_folder = source / category
                destination = get_unique_destination(
                    target_folder / file_path.name
                )

                if dry_run:
                    print(f"[DRY RUN] {file_path.name} -> {category}/{destination.name}")
                    moved += 1
                    continue

                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(destination))
                print(f"Moved: {file_path.name} -> {category}/{destination.name}")
                moved += 1

            except (PermissionError, FileExistsError, OSError) as error:
                print(f"Could not process {entry.name}: {error}")
                failed += 1

    print("\n--- Organization Summary ---")
    print(f"Files moved / previewed: {moved}")
    print(f"Files skipped: {skipped}")
    print(f"Files failed: {failed}")


def main():
    print("AUTOMATED FILE ORGANIZER")
    directory = input("Enter the folder path to organize: ").strip().strip('"')
    choice = input("Preview only? (y/n): ").strip().lower()
    dry_run = choice == "y"

    try:
        organize_directory(directory, dry_run=dry_run)
    except (ValueError, PermissionError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()