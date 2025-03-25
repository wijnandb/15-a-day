import json
from todoist_api_python.api import TodoistAPI

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Todoist API token
API_TOKEN = os.environ.get("TODOIST_API_TOKEN")
api = TodoistAPI(API_TOKEN)


# Labels to categorize tasks
URGENT_LABEL = "urgent"
IMPORTANT_LABEL = "important"

# Fetch and categorize tasks
def fetch_and_categorize_tasks():
    matrix = {
        "Q1": [],  # Urgent & Important
        "Q2": [],  # Important, Not Urgent
        "Q3": [],  # Urgent, Not Important
        "Q4": []   # Neither Urgent nor Important
    }
    try:
        tasks = api.get_tasks()
        for task in tasks:
            labels = task.labels
            task_data = {"id": task.id, "content": task.content}
            
            if URGENT_LABEL in labels and IMPORTANT_LABEL in labels:
                matrix["Q1"].append(task_data)
            elif IMPORTANT_LABEL in labels and URGENT_LABEL not in labels:
                matrix["Q2"].append(task_data)
            elif URGENT_LABEL in labels and IMPORTANT_LABEL not in labels:
                matrix["Q3"].append(task_data)
            else:
                matrix["Q4"].append(task_data)
    except Exception as e:
        print(f"An error occurred: {e}")
    return matrix

# Save tasks to JSON
def save_tasks_to_json(matrix, filename="static/html/todoist_tasks.json"):
    with open(filename, "w") as f:
        json.dump(matrix, f, indent=4)
    print(f"Tasks saved to {filename}")

if __name__ == "__main__":
    tasks_matrix = fetch_and_categorize_tasks()
    save_tasks_to_json(tasks_matrix)
