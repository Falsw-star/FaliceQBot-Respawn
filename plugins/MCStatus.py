from faliceqbot import Plugin, Message
from mcstatus import JavaServer, BedrockServer
import time

MCStatus = Plugin(
    name='MCStatus',
    version='1.0.0',
    author='Falsw',
    description="Simple Minecraft servers' status checker"
)

def java_server(ip) -> tuple[bool, str]:
    try:
        server = JavaServer.lookup(ip)
        status = server.status()
        if status.motd.raw is not None and 'text' in status.motd.raw:
            motd = status.motd.to_plain()
        else:
            motd = "(Fvck it up, I can't get it)"
        result: str = '{}\nVersion: {}\nPing: {}ms\nOnline: {}'.format(
            motd,
            status.version.name,
            round(status.latency),
            f'{status.players.online} of {status.players.max}'
        )
        if status.players.sample is not None:
            for player in status.players.sample:
                result += f'\n - {player.name}'
        return True, result
    except ConnectionError as e:
        return False, str(e)

def bedrock_server(ip) -> tuple[bool, str]:
    try:
        server = BedrockServer.lookup(ip)
        status = server.status()
        if status.motd.raw is not None and 'text' in status.motd.raw:
            motd = status.motd.to_plain()
        else:
            motd = "(Fvck it up, I can't get it)"
        result: str = '{}\nVersion: {}\nPing: {}\n Gamemode: {}\nOnline: {}'.format(
            motd,
            status.version.name,
            round(status.latency),
            status.gamemode,
            f'{status.players.online} of {status.players.max}'
        )
        return True, result
    except ConnectionError as e:
        return False, str(e)
    
def mcstatus(msg: Message):
    args = msg.get_args()
    if len(args) < 2:
        msg.respond('Usage: /mcstatus <java(j)/bedrock(b)> <ip>')
        return
    
    if args[0] == 'java' or args[0] == 'j':
        for ip in args[1:]:
            status, result = java_server(ip)
            if status:
                msg.respond(result)
            else:
                msg.respond(f'Is server {ip} offline? :(\n{result}')
            time.sleep(0.5)
    
    elif args[0] == 'bedrock' or args[0] == 'b':
        for ip in args[1:]:
            status, result = bedrock_server(ip)
            if status:
                msg.respond(result)
            else:
                msg.respond(f'Is server {ip} offline? :(\n{result}')
            time.sleep(0.5)
    
    else:
        msg.respond('Usage: /mcstatus <java/bedrock> <ip>')
        return

MCStatus.onCommand(mcstatus, ['mcstatus', 'mcs'], permission=0)

def load() -> Plugin:
    return MCStatus