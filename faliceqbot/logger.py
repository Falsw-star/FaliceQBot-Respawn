class Colors:
    BLACK = '\033[0m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    GREY = '\033[93m'
    RED = '\033[91m'
    YELLOW = '\033[33m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def paint(content: str, color) -> str:
    return (color + content + Colors.ENDC)

import time
class Tags:
    INFO = '[{}]'.format(paint("INFO", Colors.BLUE))
    SUCCESS = '[{}]'.format(paint("SUCCESS", Colors.GREEN))
    WARNING = '[{}]'.format(paint("WARNING", Colors.RED))
    ERROR = '[{}]'.format(paint("ERROR", Colors.RED))
    FAIL = '[{}]'.format(paint("FAIL", Colors.GREY))
    DEBUG = '[{}]'.format(paint("DEBUG", Colors.PURPLE))
    RUNTIME = '[{}]'.format(paint("RUNTIME", Colors.PURPLE))
    CHAT = '[{}]'.format(paint("CHAT", Colors.YELLOW))

def TimeTag() -> str:
    return '[{}]'.format(time.strftime("%H:%M:%S", time.localtime()))

def log(content: str, level: int = 0) -> None:
    """
    Logs a message to the terminal.
    LEVELS:
    0: INFO
    1: SUCCESS
    2: WARNING
    3: ERROR
    4: fail
    5: DEBUG
    6: RUNTIME
    7: CHAT
    """
    match level:
        case 0:
            print('{}{} : {}'.format(TimeTag(), Tags.INFO, content))
        case 1:
            print('{}{} : {}'.format(TimeTag(), Tags.SUCCESS, paint(content, Colors.GREEN)))
        case 2:
            print('{}{} : {}'.format(TimeTag(), Tags.WARNING, content))
        case 3:
            print('{}{} : {}'.format(TimeTag(), Tags.ERROR, paint(content, Colors.RED)))
        case 4:
            print('{}{} : {}'.format(TimeTag(), Tags.FAIL, paint(content, Colors.GREY)))
        case 5:
            print('{}{} : {}'.format(TimeTag(), Tags.DEBUG, content))
        case 6:
            print('{}{} : {}'.format(TimeTag(), Tags.RUNTIME, paint(content, Colors.PURPLE)))
        case 7:
            print('{}{} : {}'.format(TimeTag(), Tags.CHAT, paint(content, Colors.YELLOW)))


def info(content: str) -> None:
    log(content, 0)

def success(content: str) -> None:
    log(content, 1)

def warning(content: str) -> None:
    log(content, 2)

def error(content: str) -> None:
    log(content, 3)

def fail(content: str) -> None:
    log(content, 4)

def debug(content: str) -> None:
    log(content, 5)

def runtime(content: str) -> None:
    log(content, 6)

def chat(content: str) -> None:
    log(content, 7)


def add_line(file_name: str, line: str) -> None:
    with open(file_name, 'a') as f:
        f.write(line + '\n')