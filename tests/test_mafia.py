# # test_mafia.py
import json

import pytest
from typer.testing import CliRunner

from mafia import (
    DB_READ_ERROR,
    ID_ERROR,
    SUCCESS,
    __app_name__,
    __version__,
    cli,
    mafia,
)

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


@pytest.fixture
def mock_json_file(tmp_path):
    todo = [{"Description": "Get some milk.", "Done": False}]
    db_file = tmp_path / "todo.json"
    with db_file.open("w") as db:
        json.dump(todo, db, indent=4)
    return db_file


test_data1 = {
    "description": ["Clean", "the", "house"],
    "todo": {
        "Description": "Clean the house.",
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "todo": {
        "Description": "Wash the car.",
        "Done": False,
    },
}


@pytest.mark.parametrize(
    "description, expected",
    [
        pytest.param(
            test_data1["description"],
            (test_data1["todo"], SUCCESS),
        ),
        pytest.param(
            test_data2["description"],
            (test_data2["todo"], SUCCESS),
        ),
    ],
)
def test_add(mock_json_file, description, expected):
    todoer = mafia.Todoer(mock_json_file)
    assert todoer.add(description) == expected
    read = todoer._db_handler.read_todos()
    assert len(read.todo_list) == 2



