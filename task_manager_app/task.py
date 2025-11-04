class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data.get("title", ""),
            description=data.get("description", ""),
            priority=data.get("priority", "")
        )
