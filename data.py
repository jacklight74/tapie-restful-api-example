todos = []
counter = 1

def get_all_todos():
    return todos

def get_todo(todo_id: int):
    return next((todo for todo in todos if todo["id"] == todo_id), None)

def create_todo(data):
    global counter
    todo = {"id": counter, **data}
    todos.append(todo)
    counter += 1
    return todo

def update_todo(todo_id, data):
    todo = get_todo(todo_id)
    if todo:
        todo.update({k: v for k, v in data.items() if v is not None})
    return todo

def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]