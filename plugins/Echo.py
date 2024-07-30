from Falice.segments import Plugin, Message

Echo = Plugin("Echo","1.0.0","Falsw","The bot will make a repeat.")
def echo(message: Message) -> None:
    message.respond(message.get_args_string())

Echo.onCommand(echo, 'echo')

def load() -> Plugin:
    return Echo