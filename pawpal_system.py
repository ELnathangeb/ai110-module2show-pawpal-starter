from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    category: str
    completed: bool = False

    def mark_complete(self):
        """Marks this task as completed."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Adds a task to this pet."""
        pass

    def remove_task(self, task):
        """Removes a task from this pet."""
        pass

    def get_tasks(self):
        """Returns all tasks for this pet."""
        pass


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: list = field(default_factory=list)
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Adds a pet to this owner."""
        pass

    def get_all_tasks(self):
        """Returns tasks from all pets."""
        pass


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def generate_daily_plan(self):
        """Creates a daily schedule."""
        pass

    def sort_tasks(self, tasks):
        """Sorts tasks."""
        pass

    def detect_conflicts(self, tasks):
        """Detects scheduling conflicts."""
        pass