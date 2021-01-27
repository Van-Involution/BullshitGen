# -*- coding: UTF-8 -*-

from typing import *
from json import load
import random

from mcdreforged.api.all import *
from typing import List

PLUGIN_METADATA = {
    'id': 'bullshit_generator_api',
    'version': '1.0.0',
    'name': 'BullshitGenAPI.py',
    'description': '',
    'author': [
        'Van_Involution'
    ],
    'link': 'https://github.com/Van-Involution/MCDR-Plugins',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}

DATA_PATH = 'config/BullshitData.json'
DEFAULT_KEY = '§ktest§r'


def generate(keys: Union[str, List[str], Set[str]], limit: int = 5):
    if type(keys) == str:
        key_list = [keys]
    else:
        key_list = list(keys)
    with open(file=DATA_PATH, mode='r') as data_file:
        data = load(data_file)
    bosh: List[str] = data['bosh']
    before: List[str] = data['before']
    after: List[str] = data['after']
    famous: List[str] = data['famous']
    text = RTextList()
    for r in range(1, limit):
        i = random.randint(1, 100)
        if i <= 5:
            text.append('\n')
        elif i <= 10:
            text.append(random.choice(famous).format(
                before=random.choice(before),
                after=random.choice(after)
            ))
        else:
            text.append(random.choice(bosh).format(key=random.choice(key_list)))
    else:
        return text


def bullshit_say(src: CommandSource):
    server = src.get_server()
    server.broadcast(generate(DEFAULT_KEY))


def on_load(server: ServerInterface, info: Info):
    server.register_help_message(prefix='!!bullshit', message='Get a text like bullshit', permission=2)
    server.register_command(
        Literal('!!bullshit')
        .then(
            Literal('get').runs(lambda src: src.reply(generate(DEFAULT_KEY)))
        )
        .then(
            Literal('say').runs(bullshit_say)
        )
    )
