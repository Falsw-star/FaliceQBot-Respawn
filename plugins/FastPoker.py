from faliceqbot import Plugin, Message
import time

Poker = Plugin("FastPoker", load_on_launch=False)

def poke(message: Message):
    args = message.get_args()
    if not len(args) == 2:
        message.respond('Usage: /poke <qqid> <count>')
        return
    userid = int(args[0])
    count = int(args[1])
    if count > 20 and not message.get_permission() == 3:
        message.respond('Too Much...')
        return
    operatorid = message.user.id
    if message.private:
        sendmsg = message.Sender.send_private_message
        cid = message.user.id
    else:
        sendmsg = message.Sender.send_message
        cid = message.group_id
    for i in range(count):
        sendmsg(cid, f'<chronocat:poke user-id="{userid}" operator-id="{operatorid}"/>')
        time.sleep(0.1)

Poker.onCommand(poke, ['poke'])

def load():
    return Poker