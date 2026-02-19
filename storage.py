import json
from pathlib import Path

FILE = "todos.json"

def save(todo_list):
    data = {
        "active": [item.to_dict() for item in todo_list.active],
        "archived": [item.to_dict() for item in todo_list.archived],
        "next_id": todo_list.next_id
    }
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def load():
    if not Path(FILE).exists():
        from todo import TodoList
        return TodoList()

    with open(FILE) as f:
        data = json.load(f)

    from todo import TodoList, TodoItem
    todo_list = TodoList()
    todo_list.active = [TodoList.from_dict(i) for i in data["active"]]
    todo_list.archived = [TodoList.from_dict(i) for i in data["archived"]]
    todo_list.next_id = data.get("next_id", 1)
    return todo_list


