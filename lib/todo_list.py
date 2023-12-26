from lib.todo import Todo
from typing import List

class TodoList:
    def __init__(self) -> None:
        self.todos = []

    def add(self, todo: Todo) -> None:
        self.todos.append(todo)

    def incomplete(self) -> List[str]:
        return [todo for todo in self.todos if todo.complete == False]
    
    def complete(self) -> List[str]:
        return [todo for todo in self.todos if todo.complete]
