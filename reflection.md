# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages one or more pets and stores information such as available time and preferences. The Pet class stores information about an individual pet and its list of care tasks. The Task class represents a single pet care activity, including its duration, priority, category, and completion status. The Scheduler class is responsible for generating a daily care plan by organizing tasks based on priority and available time.

### b. Design changes

During implementation, I simplified some parts of the scheduler. Instead of implementing a complex scheduling algorithm with exact time slots, I sorted tasks by priority and only scheduled tasks that fit within the owner's available time. This made the project easier to implement while still meeting the core requirements.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler considers two main constraints: the owner's available time and each task's priority. High-priority tasks are scheduled first, and tasks are only added if there is enough available time remaining. I chose these constraints because they are the most important for making sure essential pet care tasks are completed.

### b. Tradeoffs

One tradeoff is that lower-priority tasks may not be included if there is not enough available time. This is reasonable because important tasks like feeding or medication should be completed before optional tasks like grooming or enrichment.

---

## 3. AI Collaboration

### a. How you used AI

I used AI to help brainstorm the class design, understand object-oriented programming concepts, debug Python code, and connect my backend classes to the Streamlit interface. The most helpful prompts asked for explanations of errors, suggestions for class structures, and examples of how to connect the UI to my scheduling logic.

### b. Judgment and verification

I did not accept every suggestion immediately. After making changes, I ran my program and my pytest tests to verify that the code worked correctly. If the output or tests did not match my expectations, I revised the implementation before continuing.

---

## 4. Testing and Verification

### a. What you tested

I tested task completion, adding tasks to pets, adding pets to owners, generating schedules, and sorting tasks by priority. These tests were important because they verified that the core functionality of my scheduling system worked correctly.

### b. Confidence

I am confident that the scheduler works correctly for the scenarios I tested. If I had more time, I would test additional edge cases such as duplicate tasks, tasks with the same priority, owners with no available time, and pets with no scheduled tasks.

---

## 5. Reflection

### a. What went well

I am most satisfied with successfully connecting my backend scheduling logic to the Streamlit interface so users can interact with the application through a graphical interface.

### b. What you would improve

If I had another iteration, I would improve the scheduling algorithm by assigning actual times to tasks, supporting recurring tasks, allowing task editing and deletion, and improving conflict detection.

### c. Key takeaway

One important thing I learned is that designing the system before writing code makes implementation much easier. I also learned that AI is most useful when used as a tool for brainstorming, debugging, and learning concepts rather than simply generating complete solutions.