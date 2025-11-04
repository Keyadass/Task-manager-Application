import json
from task_manager_app.task import Task

def read_tasks(filepath):
    try:
        with open(filepath, 'r') as f:
            raw_tasks = json.load(f)
            return [Task.from_dict(t) for t in raw_tasks]
    except FileNotFoundError:
        return []  # If no file, return empty list
    except json.JSONDecodeError:
        print("Error: Could not decode JSON. File might be corrupted.")
        return []

def write_tasks(filepath, tasks):
    with open(filepath, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)
