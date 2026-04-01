class Task:
    def __init__(self, description, time):
        self.description = description
        self.time = time
        self.completed = False

    def mark_complete(self):
        self.completed = True


class Pet:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)


class Scheduler:
    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return tasks

    def sort_by_time(self):
        return sorted(self.get_all_tasks(), key=lambda x: x.time)
