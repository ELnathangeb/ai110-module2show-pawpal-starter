from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner(name="Elnathan", available_minutes=60)

dog = Pet(name="Biscuit", species="Golden Retriever", age=3)
cat = Pet(name="Milo", species="Cat", age=2)

dog.add_task(Task("Morning walk", 30, "high", "exercise"))
dog.add_task(Task("Feeding", 10, "high", "food"))
cat.add_task(Task("Brush fur", 20, "medium", "grooming"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)
plan = scheduler.generate_daily_plan()

print("Daily Plan:")
for pet, task in plan:
    print(f"- {pet.name}: {task.name} ({task.duration} min) [priority: {task.priority}]")