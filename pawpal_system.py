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
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        """Adds a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Removes a task from this pet."""
        self.tasks.remove(task)

    def get_tasks(self):
        """Returns all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: list = field(default_factory=list)
    pets: list = field(default_factory=list)

    def add_pet(self, pet):
        """Adds a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Returns tasks from all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet, task))

        return all_tasks


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def generate_daily_plan(self):
        """Creates a daily schedule based on priority and available time."""
        tasks = self.owner.get_all_tasks()
        sorted_tasks = self.sort_tasks(tasks)

        plan = []
        used_minutes = 0

        for pet, task in sorted_tasks:
            if used_minutes + task.duration <= self.owner.available_minutes:
                plan.append((pet, task))
                used_minutes += task.duration

        return plan

    def sort_tasks(self, tasks):
        """Sorts tasks by priority."""
        priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

        return sorted(
            tasks,
            key=lambda item: priority_order.get(item[1].priority.lower(), 4)
        )

    def detect_conflicts(self, tasks):
        """Detects tasks with the same priority and category."""
        seen = set()
        conflicts = []

        for pet, task in tasks:
            key = (task.priority, task.category)

            if key in seen:
                conflicts.append(
                    f"Possible conflict: multiple {task.priority} priority {task.category} tasks."
                )
            else:
                seen.add(key)

        return conflicts