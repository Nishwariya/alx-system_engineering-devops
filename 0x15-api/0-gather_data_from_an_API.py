#!/usr/bin/python3
import urllib.request
import json
import sys

# Check if an employee ID was provided as an argument
if len(sys.argv) < 2:
    print("Please provide an employee ID as an argument.")
    sys.exit(1)

# Set the base URL for the REST API
base_url = "https://jsonplaceholder.typicode.com"

# Get the employee ID from the command line arguments
employee_id = sys.argv[1]

# Send a GET request to the REST API to get the employee's TODO list
url = f"{base_url}/todos?userId={employee_id}"
response = urllib.request.urlopen(url)

# Parse the JSON response and count the number of completed tasks
data = json.loads(response.read())
completed_tasks = [task for task in data if task["completed"]]
num_completed_tasks = len(completed_tasks)
num_total_tasks = len(data)

# Get the employee name from the REST API
url = f"{base_url}/users/{employee_id}"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
employee_name = data["name"]

# Print the employee TODO list progress
print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_total_tasks}):")
for task in completed_tasks:
    print(f"\t {task['title']}")
