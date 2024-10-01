from faliceqbot import Plugin, Message
import httpx

Netease = Plugin('Netease')

def song_search(message: Message):
    
    api_url = 'http://127.0.0.1:25565/web/netease/search/'
    
    ids = message.get_args()
    if not ids:
        message.respond('每日推荐还未完工！')
    else:
        url = '/'.join(ids)
        response = httpx.get(api_url + url).json()
        code = response['code']
        if code == 200:
            songs = response['result']['songs']
            if not songs:
                message.respond('搜不到这个啦……xwx')
                return
            song_list = '\n'.join([f'{i}. {songs[i-1]["name"]} - {"/".join([artist["name"] for artist in songs[i-1]["artists"]])} - {songs[i-1]["id"]}' for i in range(1, len(songs)+1)])
            message.respond(f'{song_list}')
        elif code == 503:
            msg = response['msg'][0]
            message.respond(f'网易云音乐API请求失败:\n{msg}\nncmrf 刷新一下试试？')
            return

def song_format(song: dict) -> str:
    result = f"""
Name: {song['name']}
<<IMAGE:{song['picUrl']}>>
ID: {song['song_id']}
Artists: {', '.join(song['arnames'])}
Album: {song['alname']}
Size: {song['size']}
Quality: {song['level']}
URL: {song['url']}
"""
    return result

def song_url(message: Message):

    api_url = 'http://127.0.0.1:25565/web/netease/url/'
    
    ids = message.get_args()
    if not ids:
        message.respond('Usage: songu (standard/exhigh/lossless) <id(s)>')
        return
    if len(ids) == 1:
        if not ids[0].isdigit():
            message.respond('Usage: songu (standard/exhigh/lossless) <id(s)>')
            return
    url = '/'.join(ids)
    response = httpx.get(api_url + url).json()
    code = response['code']
    result: list[str] = []
    if code == 200:
        data = response['result']['data']
        if not data:
            message.respond('空空的……')
            return
        for song in data:
            if song['status']:
                result.append(song_format(song))
            else:
                result.append(f'无法获取链接！\n{song["msg"]}')
    elif code == 503:
        msg = response['msg'][0]
        message.respond(f'网易云音乐API请求失败:\n{msg}\nncmrf 刷新一下试试？')
        return
    
    if len(result) == 1:
        message.respond('\n'.join(result))

def song_play(message: Message):

    api_url = 'http://127.0.0.1:25565/web/netease/url/'
    
    ids = message.get_args()
    if not ids:
        message.respond('Usage: songp (standard/exhigh/lossless) <id(s)>')
        return
    if len(ids) == 1:
        if not ids[0].isdigit():
            message.respond('Usage: songp (standard/exhigh/lossless) <id(s)>')
            return
    url = '/'.join(ids)
    response = httpx.get(api_url + url).json()
    code = response['code']
    if code == 200:
        data = response['result']['data']
        if not data:
            message.respond('空空的……')
            return
        for song in data:
            if song['status']:
                respond_id = message.user.id if message.private else message.group_id
                message.Sender.send_message(respond_id, f'<audio src=\"{song["url"]}\" duration="300" />')
            else:
                message.respond(f'无法获取链接！\n{song["msg"]}')
    elif code == 503:
        msg = response['msg'][0]
        message.respond(f'网易云音乐API请求失败:\n{msg}\nncmrf 刷新一下试试？')
        return

def refresh(message: Message):
    api_url = 'http://127.0.0.1:25565/web/netease/refresh'
    response = httpx.get(api_url).json()
    message.respond(response['msg'][0])

Netease.onCommand(song_search, ['songs', 'songsearch', 'ncms'])
Netease.onCommand(song_url, ['songu', 'songurl', 'ncmu'])
Netease.onCommand(song_play, ['songp', 'songplay', 'ncmp'])

def load():
    return Netease