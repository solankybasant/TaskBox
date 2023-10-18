# mafia/cli.py
from typing import Optional,List
from pathlib import Path
import typer
from mafia import (

        __app_name__, 
        __version__,
        ERRORS,
        config,
        database,
        mafia

        )
# print(__app_name__)

app=typer.Typer();

#define app commands
@app.command()
def init(
        db_path: str=typer.Option(
            str(database.DEFAULT_DB_FILE_PATH),
            "--db-path",
            "-db",
            prompt="what is database location :) ?",
            ),
) -> None:
    #starting the db
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
                f'Conf file failed with "{ERRORS[app_init_error]}"',
                fg=typer.colors.RED,
                )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
                f'DB failed with "{ERRORS[db_init_error]}"',
                fg.typer.colors.RED,
                )
        raise typer.Exit(1)
    else:
        typer.secho(f"DB is {db_path}", fg=typer.colors.GREEN)


def get_todoer() -> mafia.Todoer:
    if config.CONFIG_FILE_PATH.exists():
        db_path = database.get_database_path(config.CONFIG_FILE_PATH)
    else :
        typer.secho(
                "Config not found. Run ~ mafia init ",
                fg=typer.colors.RED,
        )
        raise typer.Exit(1)

    if db_path.exists():
        return mafia.Todoer(db_path)
    else:
        typer.secho(
                "DB not found. Run ~ mafia init",
                fg=typer.colors.RED,
        )
        raise typer.Exit(1)

@app.command()
def add(
        description: List[str]=typer.Argument(...),
        # priority: int=typer.Option(2,"--priority","-p",min=1,max=3),
    ) -> None:
    #Adding a new todo with description
    todoer=get_todoer()
    todo,error = todoer.add(description)
    if error:
        typer.secho(
                f'Adding task failed with"{ERRORS[error]}"',
                fg=typer.colors.RED
        )
        raise typer.Exit(1)
    else :
        typer.secho(
            # f"""to-do: "{todo['Description']}" was added """,

            f'to-do: "{todo["Description"]}" was added',
            
            fg=typer.colors.GREEN,
        )



@app.command(name="show")
def list_all()-> None:

    print("""
___________              __            __________              
\__    ___/____    _____|  | __        \______   \ _______  ___
  |    |  \__  \  /  ___/  |/ /  ______ |    |  _//  _ \  \/  /
  |    |   / __ \_\___ \|    <  /_____/ |    |   (  <_> >    < 
  |____|  (____  /____  >__|_ \         |______  /\____/__/\_ \:)
               \/     \/     \/                \/            \/
    """)
    todoer = get_todoer()
    todo_list=todoer.get_todo_list()
    if len(todo_list)==0:
        typer.secho(
            "Run python mafia add "<Task>" to add task",
            fg=typer.colors.RED
        )
        raise typer.Exit()
    typer.secho("\nTodoBox List:\n",
                fg=typer.colors.BLUE,
                bold=True
                )
    columns=(
        "ID.",
        "| Done",
        "| Description",
    )
    headers = "".join(columns)
    typer.secho(headers,
                fg=typer.colors.BLUE,
                bold=True
                )
    typer.secho(
        "-"*2*len(headers),
        fg=typer.colors.BLUE
    )
    for id, todo in enumerate(todo_list,1):
        desc,done=todo.values()
        typer.secho(
           
            
            f"{id}{(len(columns[0]) - len(str(id))) * ' '}"

            f"| {done}{(len(columns[2]) - len(str(done)) - 2) * ' '}"

            f"| {desc}",

            fg=typer.colors.BLUE,
        )   
    typer.secho("-"*2*len(headers)+"\n",
                fg=typer.colors.BLUE
                )


@app.command(name="complete")
def set_done(todo_id:int=typer.Argument(...)) ->None:
    #complete by TODO ID
    todoer=get_todoer()
    todo,error=todoer.set_done(todo_id)
    if error:
        typer.secho(
            f'TODO with ID "{todo_id}" failed with "ERRORS[error]" ',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"""Congrats, TODO with ID-> {todo_id} and description-> "{todo['Description']}", Completed!""",
            fg=typer.colors.GREEN,
        )


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool]=typer.Option(
            None,
            "--version",
            "-v",
            help="Show version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    return
