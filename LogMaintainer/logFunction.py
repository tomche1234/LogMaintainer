from datetime import datetime


class Log:
    current: datetime = datetime.now()
    COLORS = {
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "MAGENTA": "\033[35m",
        "CYAN": "\033[36m",
        "WHITE": "\033[37m",
        "RESET": "\033[0m",  # Add a reset color code
    }

    @classmethod
    def running(cls, funcitonName: str):
        """for log which funtion is running"""
        print(
            f"{cls.COLORS['YELLOW']}{cls.current}{cls.COLORS['WHITE']}:{funcitonName} is running" + cls.COLORS["RESET"]
        )

    @classmethod
    def log(cls, funcitonName: str, message: str):
        """for log message in function"""
        print(
            f"{cls.COLORS['YELLOW']}{cls.current}{cls.COLORS['WHITE']} {funcitonName}: {message}" + cls.COLORS["RESET"]
        )

    @classmethod
    def exception(cls, funcitonName: str, e: Exception):
        """for log exception"""
        print(
            f"{cls.COLORS['YELLOW']}{cls.current}{cls.COLORS['RED']}[{type(e)} error happened on {funcitonName}]:{e}"
            + cls.COLORS["RESET"]
        )
        raise e
