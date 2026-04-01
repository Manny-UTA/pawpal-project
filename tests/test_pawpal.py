from pawpal_system import Task

def test_mark_complete():
    task = Task("Feed dog", "08:00")
    task.mark_complete()
    assert task.completed == True
