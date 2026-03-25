from pathlib import Path


def main():
    file_path = [Path("sample1.txt"), Path("sample2.txt")]

    for i in range(0, len(file_path)):
        if file_path[i].exists():
            print(file_path[i].read_text())


def test_main()-> None:
    assert True 
    main()



def print_hello_world() -> None:
    print("Hello, World!")

def read_file(file_path: Path) -> str:
    if file_path.exists():
        return file_path.read_text()
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")



def write_to_file(file_path: Path, content: str) -> None:
    file_path.write_text(content)

def append_to_file(file_path: Path, content: str) -> None:
    with file_path.open("a") as f:
        f.write(content)

if __name__ == "__main__":
    main()

def add_numbers(a: int, b: int) -> int:
    return a + b


def print_greeting(name: str) -> None:
    print(f"Hello, {name}!")


def calculate_area(radius: float) -> float:
    import math
    return math.pi * radius ** 2
def find_maximum(numbers: list) -> int:
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)

def reverse_string(s: str) -> str:
    return s[::-1]

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    





    