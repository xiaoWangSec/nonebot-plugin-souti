import re
from urllib.parse import quote as urlencode

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import CommandArg

import httpx

query = on_command("搜题", priority=5)
@query.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        async with httpx.AsyncClient() as client:
            url = f"https://tiku.baidu.com/buguakewap/proxy/bgk/bigque/getwapquesearch?query={urlencode(plain_text)}&na_uncheck=1&wk_cs_app=1"
            resp = await client.get(url)
            qid = resp.json()['data']['list'][0]['qid_str']
            url = f"https://tiku.baidu.com/buguakewap/browse/index?qid={qid}&limitSwitch=1&limitTimes=3"
            resp = await client.get(url)
            answer = re.findall('pageDescription":"(.*?)","answerList":', resp.text)[0]
            await matcher.send(answer)
    else:
        await matcher.send('语法: 搜题 需要搜索的题目')
