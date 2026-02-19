from datetime import datetime

class TodoItem:
    def __init__(self, id: int, text: str):
        self.id = id
        self.text = text
        self.created = datetime.now().isoformat()
        self.completed = None
    
        def to_dict(self):
            return {"id": self.id, "text": self.text, "created": self.created, "completed": self.completed}

        @staticmethod
        def from_dict(data):
            item = TodoItem(data["id"], data["text"])
            item.created = data["created"]
            item.completed = data.get("completed")
            return item

    class TodoList:
        def __init__(self):
            self.active = []
            self.archived = []
            self.next_id = 1
        
        def add(self, text: str) -> TodoItem:
            item = TodoItem(self.next_id, text)
            self.next_id += 1
            self.active.append(item)
            return item

        def completed(self, id:int) -> bool:
            for item in self.active:
                if item.id == id:
                    item.completed = datetime.now().isoformat()
                    self.archived.append(item)
                    self.active.remove(item)
                    return True
            return False

        def delete(self, id: int) -> bool:
            for item in self.active:
                if item.id == id:
                    self.active.remove(item)
                    return True
            return False

        def list_active(self):
            return self.active
    
        def list_archived(self):
            return self.archived

pass
