import os


def file_to_lines(file_name: str) -> list[str]:
    path = os.path.join('inputs', file_name)
    try:
        with open(path, 'r') as file:
            lines = file.read().splitlines()
            return lines
    except FileNotFoundError:
        print(f"My brother in Christ, there is no file called {file_name}")
        return []


def file_to_str(file_name: str) -> str:
    path = os.path.join('inputs', file_name)
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"My brother in Christ, there is no file called {file_name}")
        return ''
