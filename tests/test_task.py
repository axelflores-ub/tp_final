import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from task import Task

def test_create_task():
    task = Task("Estudiar", "Alta")

    assert task.description == "Estudiar"
    assert task.priority == "Alta"