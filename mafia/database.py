# database.py

import configparser
from pathlib import Path

from mafia import (
        DB_WRITE_ERROR,
        SUCCESS
        )

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
        "." + Path.home().stem + "_todo.json"
        )

def get_database_path(config_file: Path) -> Path:

    #return the curr path to the to-do database.
    config_parser = configparser.ConfigPatser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path)->int:
    try:
        #initially empty
        db_path.write_text("[]")
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
