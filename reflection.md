# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages multiple pets, the Pet class stores information about each pet and its tasks, the Task class represents individual activities like feeding or walking, and the Scheduler organizes tasks across pets. Each class was designed to reflect real-world responsibilities in a simple and modular way.

**b. Design changes**

During implementation, I simplified my design to focus on core functionality. Initially, I considered adding more complex relationships and features, but I decided to keep the structure minimal so that the system would be easier to implement and debug. This made the code more readable and easier to manage.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers time as the main constraint by sorting tasks based on their scheduled time. I prioritized time because it is the most important factor for organizing daily pet care tasks in a simple system.

**b. Tradeoffs**

One tradeoff I made was not implementing conflict detection or overlapping task handling. While this limits the system’s ability to manage complex schedules, it keeps the implementation simple and ensures the core functionality works correctly.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools to help structure my class design, generate starter code, and debug issues. AI was especially helpful in organizing the relationships between classes and suggesting cleaner implementations for functions.

**b. Judgment and verification**

There were times when AI suggested more complex solutions than necessary. I chose to simplify those suggestions to keep the system easier to understand and maintain. I verified AI suggestions by testing the code and making sure it worked as expected.

---

## 4. Testing and Verification

**a. What you tested**

I tested basic behaviors such as adding tasks to pets, storing pets under an owner, and sorting tasks by time. These tests were important to ensure the system correctly organizes and displays the schedule.

**b. Confidence**

I am moderately confident that my scheduler works for basic use cases. If I had more time, I would test edge cases such as empty task lists, duplicate times, and invalid inputs.

---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is the class structure. The system is modular and clearly separates responsibilities between different components.

**b. What you would improve**

If I had another iteration, I would improve the scheduler by adding conflict detection and support for recurring tasks. I would also enhance the UI integration.

**c. Key takeaway**

One key takeaway from this project is that designing a clean system structure is just as important as writing the code. Working with AI also showed me the importance of reviewing and simplifying suggestions instead of blindly accepting them.
