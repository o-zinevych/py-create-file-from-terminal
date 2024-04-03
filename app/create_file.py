import sys
import os
from datetime import datetime

terminal_data = sys.argv


def make_directories(dirs: list) -> None:
    return os.makedirs(os.path.join(*dirs))


def input_file_contents(path_name: str) -> None:
    with open(path_name, "a") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time_now)
        line_num = 0
        while True:
            line_num += 1
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.write(f"\n{line_num} {content}\n")


if "-d" in terminal_data and "-f" in terminal_data:
    directories = terminal_data[2:-2]
    make_directories(directories)
    file_name = terminal_data[-1]
    joined_path = os.path.join(*directories, file_name)
    input_file_contents(joined_path)

elif "-d" in terminal_data:
    directories = terminal_data[2:]
    make_directories(directories)

elif "-f" in terminal_data:
    file_name = terminal_data[-1]
    input_file_contents(file_name)
