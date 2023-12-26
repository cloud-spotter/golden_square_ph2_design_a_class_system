class Todo:
    def __init__(self, task) -> None:
        self.task = task
        self.complete = False

    def mark_complete(self) -> None:
        self.complete = True