
from flask import Flask
import Task1, Task2, Task3, calculator  

app = Flask(_name_)

@app.route("/")
def home():
    return "Welcome! Flask with your Python tasks."

@app.route("/task1")
def run_task1():
    return str(Task1.some_function())  

@app.route("/task2")
def run_task2():
    return str(Task2.some_function())

