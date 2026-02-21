from pathlib import Path


def main():
    file_path = [Path("sample1.txt"), Path("sample2.txt")]

    for i in range(0, len(file_path)):
        if file_path[i].exists():
            print(file_path[i].read_text())
