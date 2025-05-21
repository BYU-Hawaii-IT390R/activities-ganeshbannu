from pathlib import Path
import random
import string

# Base directory for testing
BASE = Path("test_root")

# Define subfolders to create
folders = [
    BASE / "docs",
    BASE / "logs",
    BASE / "docs/subfolder",
    BASE / "logs/archive"
]

# Create folders
for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Create .txt files in each folder with random content
for i in range(5):  # 5 files per folder
    for folder in folders:
        filename = folder / f"file{i}.txt"
        content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))  # 100-character content
        filename.write_text(content)

print(f"✅ Test directories and files created under: {BASE.resolve()}")
