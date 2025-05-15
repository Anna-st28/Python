import requests
import csv
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()

with open('todos.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['userId', 'id', 'title', 'completed'])

    for item in data:
        writer.writerow([item['userId'], item['id'], item['title'], item['completed']])
