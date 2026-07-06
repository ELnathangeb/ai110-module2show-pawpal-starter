from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete():
    task = Task("Feed", 10, "high", "food")

    task.mark_complete()

    assert task.completed is True


def test_add_task():
    pet = Pet("Biscuit", "Dog", 3)

    pet.add_task(Task("Walk", 30, "high", "exercise"))

    assert len(pet.tasks) == 1


def test_add_pet():
    owner = Owner("Elnathan", 60)

    pet = Pet("Biscuit", "Dog", 3)

    owner.add_pet(pet)

    assert len(owner.pets) == 1


def test_generate_schedule():
    owner = Owner("Elnathan", 60)

    pet = Pet("Biscuit", "Dog", 3)

    pet.add_task(Task("Walk", 30, "high", "exercise"))
    pet.add_task(Task("Feed", 10, "medium", "food"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)

    plan = scheduler.generate_daily_plan()

    assert len(plan) == 2


def test_sort_priority():
    owner = Owner("Elnathan", 60)

    pet = Pet("Biscuit", "Dog", 3)

    pet.add_task(Task("Low Task", 10, "low", "misc"))
    pet.add_task(Task("High Task", 10, "high", "misc"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)

    sorted_tasks = scheduler.sort_tasks(owner.get_all_tasks())

    assert sorted_tasks[0][1].priority == "high"