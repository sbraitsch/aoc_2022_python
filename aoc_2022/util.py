import os, time


def file_to_lines(file_name: str) -> list[str]:
    path = os.path.join("inputs", file_name)
    try:
        with open(path, "r") as file:
            lines = file.read().splitlines()
            return lines
    except FileNotFoundError:
        print(f"My brother in Christ, there is no file called {file_name}")
        return []


def file_to_str(file_name: str) -> str:
    path = os.path.join("inputs", file_name)
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"My brother in Christ, there is no file called {file_name}")
        return ""


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"Execution time for {func.__name__}: {execution_time:.3f} ms")
        return result

    return wrapper
