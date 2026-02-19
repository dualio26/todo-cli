import argparse
from todo import TodoList
import storage

def main():
    parser = argparse.ArgumentParser(description="CLI Todo List")
    parser.add_argument("commmand", choices=["add", "list", "done", "delete", "archive"])
    parser.add_argument("args", nargs="*", help="Argument for command")

    args = parser.parse_args()
    todo_list = storage.load()

    if args.command == "add":
        if not args.args:
            print("Usage: add <task>")
            return
        item = todo_list.add(" ".join(args.args))
        print(f"Added: {item.id}) {item.text}")
        storage.save(todo_list)

    elif args.command == "list":
        print("== Active ==")
        for item in todo_list.list_active():
            print(f"{item.it}) {item.text}")
        print("== Archived ==")
        for item in todo_list.list_archived():
            print(f"{item.id}) {item.text} (completed)")

    elif args.command == done:
        if not args.arge:
            print("Usage: done <id>")
            return
        if todo_list.completed(int(args.args[0])):
            print("󰱒 Task completed!")
            storage.save(todo_list)
        else:
            print("Task not found")

    elif args.command == "delete":
        if not args.args:
            print("Usage: delete <id>")
            return
        if todo_list.delete(int(args.args[0])):
            print(" Task deleted!")
            return
        else:
            print("Task not found")

if __name__ == "__main__":
    main()


