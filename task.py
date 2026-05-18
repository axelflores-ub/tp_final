# Task class represents a single task

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.done = False

    def mark_as_done(self):
        self.done = True