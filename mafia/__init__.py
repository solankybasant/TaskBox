# Top level package for todo

__app_name__ = "TaskBox"
__version__ = "0.1.0"

(
        SUCCESS,
        DIR_ERROR,
        FILE_ERROR,
        DB_READ_ERROR,
        DB_WRITE_ERROR,
        JSON_ERROR,
        ID_ERROR
)=range(7)

ERRORS= {
        DIR_ERROR: "Config Dir error",
        FILE_ERROR: "Config file error",
        DB_READ_ERROR: "DB read error",
        DB_WRITE_ERROR: "DB write error",
        ID_ERROR: "mafia id error"
}
