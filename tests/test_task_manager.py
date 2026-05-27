import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task_manager import TaskManager


def test_add_task():
    manager = TaskManager()

    manager.add_task("Estudiar", "High")

    assert len(manager.tasks) == 1
    
    
def test_task_content():
    manager = TaskManager()

    manager.add_task("Estudiar", "High")

    assert manager.tasks[0].description == "Estudiar"
    assert manager.tasks[0].priority == "High"
    
    
def test_add_multiple_tasks():
    manager = TaskManager()

    manager.add_task("Estudiar", "High")
    manager.add_task("Practicar testing", "Medium")

    assert len(manager.tasks) == 2


def test_invalid_priority_not_added():
    manager = TaskManager()

    manager.add_task("Estudiar", "Alta")

    assert len(manager.tasks) == 0
    
    
def test_delete_task():
    manager = TaskManager()

    manager.add_task("Python", "High")
    manager.delete_task(0)

    assert len(manager.tasks) == 0
    
    
def test_complete_task():
    manager = TaskManager()

    manager.add_task("Python", "High")
    manager.complete_task(0)

    assert manager.tasks[0].done == True
    
    
    
def test_multiple_operations():
    manager = TaskManager()

    for i in range(50):
        manager.add_task(f"Task {i}", "High")

    assert len(manager.tasks) == 50