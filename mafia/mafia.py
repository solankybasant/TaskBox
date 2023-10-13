#mafia.py
#format
# todo = {
#     "Description": "Get some milk.",
#     "Priority": 2,
#     "Done": True,
# }
from pathlib import Path
from typing import (
        Any,
        Dict,
        NamedTuple
        )
from mafia.database import DatabaseHandler
class CurrentTodo(NamedTuple):
    todo: Dict[str,Any]
    error: int

class Todoer:
    def __init__(self,db_path:Path)->None:
        self._db_handler =DatabaseHandler(db_path)
    
