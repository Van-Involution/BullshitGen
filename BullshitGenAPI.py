# -*- coding: UTF-8 -*-

from typing import *
from json import load
from typing import List
from random import randint, choice

from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'bullshit_generator_api',
    'version': '1.0.0',
    'name': 'BullshitGenAPI',
    'description': '',
    'author': [
        'Van_Involution'
    ],
    'link': 'https://github.com/Van-Involution/BullshitGenAPI',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}

DEFAULT_DATA_PATH = 'config/BullshitData.json'
DEFAULT_KEY = '§ktest§r'
DEFAULT_PREFIX = '!!bullshit'
REPO_URL = PLUGIN_METADATA['link']


def generate(keys: Union[str, List[str], Set[str]] = DEFAULT_KEY, limit: int = 200, famous_chance: int = 10):
    if type(keys) == str:
        key_list = [keys]
    else:
        key_list = list(keys)
    with open(file=DEFAULT_DATA_PATH, mode='r') as data_file:
        data = load(data_file)
    title = RText('[§e§l§m狗屁不通文章§r]').h(f'§lDocument§r: §n{REPO_URL}§r').c(RAction.open_url, REPO_URL)
    text = '\n '
    while len(text) < limit:
        if randint(1, 100) <= famous_chance:
            text += choice(data['famous']).format(
                says=choice(data['says']),
                sothat=choice(data['sothat'])
            )
        else:
            text += choice(data['bosh']).format(key=choice(key_list))
    return RTextList(title, text)


def show_help_message(src: CommandSource):
    src.reply(RTextList(
        RText(f'§7{DEFAULT_PREFIX} get§r 获取一段狗屁不通文章\n').c(RAction.suggest_command, f'{DEFAULT_PREFIX} get'),
        RText(f'§7{DEFAULT_PREFIX} say§r 广播一段狗屁不通文章\n').c(RAction.suggest_command, f'{DEFAULT_PREFIX} say')
    ))


def on_load(server: ServerInterface, prev):
    server.register_help_message(prefix='!!bullshit', message='Get a text like bullshit', permission=2)
    server.register_command(
        Literal('!!bullshit')
        .runs(show_help_message)
        .then(
            Literal('get').runs(lambda src: src.reply(generate()))
        )
        .then(
            Literal('say').runs(lambda src: src.get_server().broadcast(generate()))
        )
    )
