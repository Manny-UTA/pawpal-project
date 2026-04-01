from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Manny")

dog = Pet("Dog")
cat = Pet("Cat")

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Feed dog", "08:00"))
dog.add_task(Task("Walk dog", "09:00"))
cat.add_task(Task("Feed cat", "07:30"))

scheduler = Scheduler(owner)

print("Today's Schedule:")
for task in scheduler.sort_by_time():
    print(task.time, "-", task.description)
