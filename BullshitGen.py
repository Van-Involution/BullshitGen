# -*- coding: UTF-8 -*-

from typing import Union, Set, List
from random import random, choice
from json import load
from re import sub

from mcdreforged.api.command import Literal, Integer, GreedyText
from mcdreforged.api.types import ServerInterface
from mcdreforged.api.rtext import RText, RTextTranslation, RTextList, RAction

PLUGIN_METADATA = {
    'id': 'bullshit_generator',
    'version': '1.0.1',
    'name': 'BullshitGen',
    'description': '狗屁不通文章生成器API (Chinese Lipsum API)',
    'author': [
        'Van_Involution'
    ],
    'link': 'https://github.com/Van-Involution/BullshitGen',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}

DEFAULT_DATA_PATH = 'config/BullshitData.json'
DEFAULT_TITLE = '§e§l§m狗屁不通文章§r'
DEFAULT_PREFIX = '!!bullshit'
DEFAULT_KEY = '§6§l§ktest§r'
REPO_URL = PLUGIN_METADATA['link']


def generate(keys: Union[str, List[str], Set[str]] = DEFAULT_KEY, limit: int = 114, famous_chance: float = 51.4, bosh_chance: float = 191.9, breakline_chance: float = 8.10):
    if type(keys) == str:
        key_list = [keys]
    else:
        key_list = list(keys)
    with open(file=DEFAULT_DATA_PATH, mode='r') as data_file:
        data = load(data_file)
    title = RText(f'[{DEFAULT_TITLE}]').h(f'§lDocs§r: §n{REPO_URL}§r').c(RAction.open_url, REPO_URL)
    text = '\n '
    while len(text) < abs(limit):
        ran = random()
        total_chance = abs(famous_chance) + abs(bosh_chance) + abs(breakline_chance)
        if ran <= abs(famous_chance) / total_chance:
            text += choice(data['famous']).format(
                says=choice(data['says']),
                sothat=choice(data['sothat'])
            )
        elif ran >= (total_chance - abs(bosh_chance)) / total_chance:
            text += choice(data['bosh']).format(key=choice(key_list))
        else:
            text += '\n '
    return RTextList(
        title, RText(text)
        .h(RTextTranslation('chat.copy.click'))
        .c(RAction.copy_to_clipboard, sub(r'§[0-9a-fk-or]', '', RText(text).to_plain_text().strip())), '\n'
    )


def on_load(server: ServerInterface, prev):
    server.register_help_message(
        DEFAULT_PREFIX,
        RText('§b[<字数>]§r §e[<关键词>]§r 生成狗屁不通文章')
        .h(f'所有参数均为可选, 可填写多个§e关键词§r, 以空格分隔\n填写§e关键词§r之前需填写整数形式的§b字数§r\n若未填写任何参数, 则以{DEFAULT_KEY}为§e关键词§r生成§b200字§r的文章')
    )
    server.register_command(
        Literal(DEFAULT_PREFIX)
        .runs(lambda src: src.reply(generate(limit=200)))
        .then(
            Integer('limit')
            .runs(lambda src, ctx: src.reply(generate(limit=ctx['limit'])))
            .then(
                GreedyText('keys')
                .runs(lambda src, ctx: src.reply(generate(limit=ctx['limit'], keys=ctx['keys'].split())))
            )
        )
    )
