# -*- coding: UTF-8 -*-

from typing import Union, Set, List
from random import random, choice
from json import load
from re import sub

from mcdreforged.api.rtext import RText, RTextTranslation, RTextList, RAction

PLUGIN_METADATA = {
    'id': 'bullshit_generator_api',
    'version': '1.0.0',
    'name': 'BullshitGenAPI',
    'description': '狗屁不通文章生成器API (Chinese Lipsum API)',
    'author': [
        'Van_Involution'
    ],
    'link': 'https://github.com/Van-Involution/BullshitGenAPI',
    'dependencies': {
        'mcdreforged': '>=1.0.0'
    }
}

DEFAULT_DATA_PATH = 'config/BullshitData.json'
REPO_URL = PLUGIN_METADATA['link']


def generate(keys: Union[str, List[str], Set[str]] = '§ktest§r', limit: int = 114, famous_chance: float = 51.4, bosh_chance: float = 191.9, breakline_chance: float = 8.10):
    if type(keys) == str:
        key_list = [keys]
    else:
        key_list = list(keys)
    with open(file=DEFAULT_DATA_PATH, mode='r') as data_file:
        data = load(data_file)
    title = RText('[§e§l§m狗屁不通文章§r]').h(f'§lDocument§r: §n{REPO_URL}§r').c(RAction.open_url, REPO_URL)
    text = '\n '
    while len(text) <= limit:
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
        title,
        RText(text)
        .h(RTextTranslation('chat.copy.click'))
        .c(RAction.copy_to_clipboard, sub(r'§[0-9a-fk-or]', '', RText(text).to_plain_text().strip()))
    )
