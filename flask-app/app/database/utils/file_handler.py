import json
import os


def read_json(filename):
    """Read data from a JSON file and ensure it's a list."""
    if not os.path.exists(filename):
        return []  # Return an empty list if the file doesn't exist

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Ensure the data is a list
    return data if isinstance(data, list) else []


def write_json(filename, data):
    """Write data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    # print(f"Written data to {filename}: {data}")  # Debug: Log the data being written


def append_json(filename, new_entry):
    data = read_json(filename)  # Ensure data is a list
    #print(f"Read data from {filename}: {data}")  # Debug: Log the data read from file
    data.append(new_entry)  # Append new entry
    write_json(filename, data)
    #print(f"Appended new entry to {filename}: {new_entry}")  # Debug: Log the new entry
