from faliceqbot import Message, Plugin
import random

NO = Plugin('NO', '1.0.0', 'NOOOOOOO')
def no(msg: Message) -> None:
    raise random.choice([Exception, ValueError, TypeError, AttributeError, KeyError, IndexError, NotImplementedError, RuntimeError, AssertionError, NameError, SyntaxError, ZeroDivisionError, OverflowError])('NOOOOO!!!')

NO.onCommand(no, 'NO', 0)

def load() -> Plugin:
    return NO