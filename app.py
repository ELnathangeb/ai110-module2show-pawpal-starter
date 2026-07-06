import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.write("Plan daily pet care tasks based on time and priority.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.subheader("Owner + Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
available_minutes = st.number_input("Available minutes today", min_value=1, max_value=480, value=60)

pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Pet age", min_value=0, max_value=30, value=3)

st.divider()

st.subheader("Add Tasks")

task_name = st.text_input("Task name", value="Morning walk")
duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
priority = st.selectbox("Priority", ["high", "medium", "low"])
category = st.text_input("Category", value="exercise")

if st.button("Add task"):
    st.session_state.tasks.append(
        {
            "name": task_name,
            "duration": int(duration),
            "priority": priority,
            "category": category,
        }
    )
    st.success(f"Added task: {task_name}")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    owner = Owner(owner_name, int(available_minutes))
    pet = Pet(pet_name, species, int(age))

    for task_data in st.session_state.tasks:
        task = Task(
            task_data["name"],
            task_data["duration"],
            task_data["priority"],
            task_data["category"],
        )
        pet.add_task(task)

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    plan = scheduler.generate_daily_plan()

    if plan:
        st.success("Daily schedule generated!")

        schedule_rows = []
        for pet, task in plan:
            schedule_rows.append(
                {
                    "Pet": pet.name,
                    "Task": task.name,
                    "Duration": task.duration,
                    "Priority": task.priority,
                    "Reason": f"Chosen because it is {task.priority} priority and fits in today's available time.",
                }
            )

        st.table(schedule_rows)
    else:
        st.warning("No tasks fit into the available time.")