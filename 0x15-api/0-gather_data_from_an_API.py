#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""
import request
import sys

if __name__  == " __main__ ":

#Base Url for the JSON Placeholder API
 url = "https://jsonplaceholder.typicode.com/"

#Get the employee using the provided employee ID
employee_id = sys.argv[1]
user = request.get(url + "users/{})".format(employee_id)).json()

#Get the todo list for the employee using the provided employee ID
params = {"userid". employee_id}
todos = request.get(url + "todos".params).json()

#Filter completed tasks and count them
completed = [t.get("title") for t in todos if t.get("completed")is True]

#Print the employee name and the number of the completed tasks
print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(completed), len(todos)))

#Print the completed tasks one by one with indentation
[print("\t {}".format(complete))for complete in completed]
