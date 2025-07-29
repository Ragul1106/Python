class PendingIterator:
    def __init__(self, tasks):
        self.tasks = [t for t in tasks if not t.status]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tasks):
            raise StopIteration
        task = self.tasks[self.index]
        self.index += 1
        return task
