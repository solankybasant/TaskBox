
# TaskBox

Developed and implemented a command-line interface application using the Typer framework to streamline and enhance task management for Linux users.



## Features


- Add new tasks to your ToDo list
- Mark tasks as completed

- List all tasks
- Remove completed tasks or clear the entire list
## Installation

TaskBox is written in Python and relies on the typer library for creating the CLI. To install TaskBox, follow these simple steps:
1. Clone the TaskBox repository or download the source code:
```bash
https://github.com/solankybasant/TaskBox
```
2. Navigate to the TaskBox directory:
```bash
cd TaskBox

```
3. Install the required dependencies using pip:

```bash 
pip install -r requirements.txt
```


    
## Usage/Examples
1. To add a new task:
```python
python -m mafia add <taskName>
```
2. To mark a task as completed:
```python
python -m mafia complete <taskNumber>
```
3. To list all tasks:
```python
python -m mafia show
```
4. To remove a task:
```python
python -m rm <taskNumber>
```
5. To reset the database:
```python 
python -m mafia reset
```
6. To set a database location:
```python
python -m mafia init
```
To remove forcefully (without confirmation)
```python
python -m mafia reset --force
```

For a complete list of commands, use the --help flag with TaskBox:
```python 
python -m mafia --help
```



