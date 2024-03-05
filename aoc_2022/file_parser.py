import os

def file_to_lines(file_name: str):
    path = os.path.join('inputs', file_name)
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"My brother in Christ, there is no file called {file_name}")
        return []
