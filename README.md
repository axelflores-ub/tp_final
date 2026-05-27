# PrioryTask

PrioryTask is a task manager application developed in Python using an object-oriented programming approach.

The project was created as part of the Final QA Project and includes automated testing using pytest.

---

## Features

- Create tasks
- Assign priority levels
- Complete tasks
- Delete tasks
- View registered tasks
- Input validation
- Automated testing with pytest
- Console-based interaction

---

## Technologies Used

- Python 3
- Pytest
- Git & GitHub
- Visual Studio Code

---

## Project Structure

```bash
tp_final/
│
├── main.py
├── task.py
├── task_manager.py
│
├── tests/
│   ├── test_task.py
│   └── test_task_manager.py
│
├── uml_priorytask_tp_final.png
├── README.md
├── TP Final Sprint 1 Documentación.pdf
├── TP Final Sprint 2 Documentación.pdf
└── TP Final Sprint 3 Documentación.pdf
```

---

## UML Diagram

This UML diagram represents the structure and relationships between the classes used in the project.

![UML Diagram](./uml_priorytask_tp_final.png)

---

## How to Run the Application

### Requirements

- Python 3.10 or higher

### Execute the application

```bash
python main.py
```

---

## Automated Testing

The project includes automated tests implemented with pytest.

### Install pytest

```bash
python -m pip install pytest
```

### Run tests

```bash
pytest
```

### Executed Test Cases

- Task creation
- Add task validation
- Invalid priority validation
- Complete task functionality
- Delete task functionality
- Multiple task operations

### Test Result

```bash
8 passed in 0.07s
```

---

## Architecture

### Task Class

Represents a task and stores:

- Description
- Priority
- Completion status

### TaskManager Class

Responsible for:

- Adding tasks
- Completing tasks
- Deleting tasks
- Managing task storage
- Validating priorities

### Main Module

Handles user interaction through the console interface.

---

## Sprint Progress

### Sprint 1
- Project initialization
- UML design
- Base architecture

### Sprint 2
- Core functionality implementation
- Test case definition

### Sprint 3
- Automated testing implementation
- Pytest integration
- Execution of defined test cases

---

## Documentation

Included in the repository:

- Sprint 1 Documentation
- Sprint 2 Documentation
- Sprint 3 Documentation
- UML Diagram

---

## Author

Developed by:

- Axel Gutkowski