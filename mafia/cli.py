# mafia/cli.py
from typing import Optional
from pathlib import Path
import typer
from mafia import (

        __app_name__, 
        __version__,
        ERRORS,
        config,
        database

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
                fg=typer.colors.BLUE,
                )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
                f'DB failed with "{ERRORS[db_init_error]}"',
                fg.typer.colors.BLUE,
                )
        raise typer.Exit(1)
    else:
        typer.secho(f"DB is {db_path}", fg=typer.colors.GREEN)




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
