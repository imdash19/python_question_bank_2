# A task list contains ['Task1','Task2']. 
# Take a new urgent task and insert it at the beginning of the list. 
# Print the updated list.

tasks = ['Task1', 'Task2']

urgent_task = input()

tasks.insert(0, urgent_task)

print(tasks)
