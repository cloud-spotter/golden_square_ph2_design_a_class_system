from lib.todo_list import TodoList
from lib.todo import Todo

"""
1. When two new Todo instances are added to a TodoList instance,
TodoList retrieves and returns these as incomplete
"""
def test_todo_list_integration_returns_all_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Codewars practice")
    todo_2 = Todo("Recap Golden Square material")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]

"""
2. When a Todo is added to the TodoList and marked as complete,
the complete and incomplete methods should reflect this change
"""
def test_todo_list_integration_add_and_mark_complete():
    todo_list = TodoList()
    todo_1 = Todo("Codewars practice")
    todo_2 = Todo("Recap Golden Square material")
    todo_3 = Todo("More codewars practice")
    todo_4 = Todo("Complete X task")
    todo_1.mark_complete()
    todo_2.mark_complete()
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_list.add(todo_4)

    assert todo_list.incomplete() == [todo_3, todo_4]
    assert todo_list.complete() == [todo_1, todo_2]