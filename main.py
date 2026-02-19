import argparse
import sys
from todo import TodoList
import storage
import ui


def print_menu():
    print("=== TODO LIST ===")
    print()

    todo_list = storage.load()

    print("Active Tasks:")
    for item in todo_list.list_active():
        print(f" {item.id}) {item.text}")

    if not todo_list.list_active():
        print("  (no Active tasks)")

    print()
    print("Archived Tasks:")
    for item in todo_list.list_archived():
        print(f" {item.id} {item.text} (completed)")
            
    if not todo_list.list_archived():
        print(" (no Archived tasks)")

    print()
    print("-" * 40)
    print("commands: add <text> | done <id> | delete <id> | exit")
    print("-" * 40)

def interactive_mode():
    while True:
        todo_list = storage.load()
        ui.clear_screen()
        print_menu()

        try:
            cmd = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if not cmd:
            continue
        
        parts = cmd.split(maxsplit=1)
        command = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if command == "exit":
            break

        elif command == "add":
            if arg:
                item = todo_list.add(arg)
                print(f"Added: {item.text}")
                storage.save(todo_list)
            else:
                print("Usage: add <task>")

        elif command == "done":
            if arg and arg.isdigit():
                if todo_list.completed(int(arg)):
                    print("Task Completed!")
                    storage.save(todo_list)
                else:
                    print("Task not found")
            else:
                print("Usage: done <id>")

        elif command == "delete":
            if arg and arg.isdigit():
                if todo_list.delete(int(arg)):
                    print("Task deleted!")
                    storage.save(todo_list)
                else:
                    print("Task not found")
            else:
                print("Usage: delete <id>")

        elif command == "help":
            print(f"Unknown command: {command}")

        input("\nPress Enter to continue...")

def main():
    parser = argparse.ArgumentParser(description="CLI Todo List")
    parser.add_argument("command", nargs="?", choices=["add", "list", "done", "delete", "archive", "interactive", help="Command to run"])
    parser.add_argument("args", nargs="*", help="Argument for command")

    args = parser.parse_args()

    if args.command is None or args.command == "interactive":
        interactive_mode()
        return

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
            print(f"{item.id}) {item.text}")
        print("== Archived ==")
        for item in todo_list.list_archived():
            print(f"{item.id}) {item.text} (completed)")

    elif args.command == "done":
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


