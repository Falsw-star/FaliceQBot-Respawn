from faliceqbot import Plugin, Message
import json, base64, requests

MCSkin = Plugin(
    name='MCSkin',
    version='1.0.0',
    author='Falsw',
    description='Get mc skins from mojang or littleskin',
    load_on_launch=True
)

def littleskin(name) -> tuple[bool, str]:
    try:
        rsp = requests.get("https://littleskin.cn/csl/" + name + ".json", timeout = 5).json()['skins']
        if('slim' in rsp.keys()):
            return True, "https://littleskin.cn/textures/" + rsp['slim']
        elif('default' in rsp.keys()):
            return True, "https://littleskin.cn/textures/" + rsp['default']
        else:
            return False, 'Cannot find skin'
    except TimeoutError:
        return False, 'Timed out'
    except KeyError:
        return False, 'Cannot find skin'

def mojang(name) -> tuple[bool, str]:
    try:
        rsp = requests.get("https://api.mojang.com/users/profiles/minecraft/" + name, timeout = 5).json()
        if('errorMessage' in rsp.keys()):
            return False, rsp['errorMessage']
        elif('id' in rsp.keys()):
            rsp = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/" + rsp['id'], timeout = 5).json()
            dc = rsp['properties'][0]['value']
            dc = json.loads(base64.b64decode(dc))
            return True, dc['textures']['SKIN']['url']
        else:
            return False, "Cannot find skin"
    except TimeoutError:
        return False, 'Timed out'

def skin(msg: Message):
    if args := msg.get_args():
        for name in args:
            littleskin_status, littleskin_msg = littleskin(name=name)
            mojang_status, mojang_msg = mojang(name=name)
            result =  '[Player name: {}]\n\nLittleskin: {}\n\nMojang: {}'.format(
                name,
                f'\n<<IMAGE:{littleskin_msg}>>\n{littleskin_msg}' if littleskin_status else littleskin_msg,
                f'\n<<IMAGE:{mojang_msg}>>\n{mojang_msg}' if mojang_status else mojang_msg
            )
            msg.respond(result)
    else:
        msg.respond('Usage: /skin <name>')

MCSkin.onCommand(skin, commands='skin', permission=0)

def load() -> Plugin:
    return MCSkin