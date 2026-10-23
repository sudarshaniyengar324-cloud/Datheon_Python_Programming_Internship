import tempfile
import unittest
from pathlib import Path

from task3.organizer import get_category, get_unique_destination, organize_directory


class OrganizerTests(unittest.TestCase):

    def test_document_category(self):
        self.assertEqual(get_category(Path("notes.pdf")), "Documents")

    def test_image_category(self):
        self.assertEqual(get_category(Path("photo.PNG")), "Images")

    def test_code_category(self):
        self.assertEqual(get_category(Path("script.py")), "Code")

    def test_unknown_category(self):
        self.assertEqual(get_category(Path("file.xyz")), "Other")

    def test_unique_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            original = folder / "notes.txt"
            original.write_text("first")

            result = get_unique_destination(original)

            self.assertEqual(result.name, "notes_1.txt")
            self.assertTrue(original.exists())

    def test_dry_run_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            sample = folder / "notes.txt"
            sample.write_text("test document")

            organize_directory(folder, dry_run=True)

            self.assertTrue(sample.exists())
            self.assertFalse((folder / "Documents").exists())

    def test_organize_file(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            sample = folder / "notes.txt"
            sample.write_text("test document")

            organize_directory(folder, dry_run=False)

            self.assertTrue((folder / "Documents" / "notes.txt").exists())
            self.assertFalse(sample.exists())


if __name__ == "__main__":
    unittest.main()