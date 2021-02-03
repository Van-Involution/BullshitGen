# BullshitGen

**English** | [中文](README_cn.md)

> **Note**: BullshitGen is developed based on [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged), and **DO NOT** support MCDR v0.x

**BullshitGen** is a MCDR plugin, which transplanted code and data from [menzi11](https://github.com/menzi11)/[**BullshitGenerator**](https://github.com/menzi11/BullshitGenerator) to MCDR platform, provide command `!!bullshit` to generate copyable **bullshit article** with customizable word count and key words in chat bar, and customized **bullshit article** generator function `generate()` which can be called by other plugins.

> ### What is **bullshit article**?
> You can think of it as **Chinese Lipsum**,, and it was first invented for Chinese typesetting testing with some funny effect, but it's **NOT offical** Chinese filling text.

## Installation

### Latest Release

Download latest `BullshitGen.zip` from [**Releases Page**](https://github.com/Van-Involution/BullshitGen/releases) and unzip it, then put `BullshitGen.py` into `plugins/` directory, and `BullshitData.json` into `config/` directory.

### Latest Source Code

Clone this repository (`git clone`) into `plugins/` directory, put a copy of `BullshitData.json` into `config/` directory, then edit `config.yml` of **MCDR instance** as the following codeblock:

```YAML
# The list of directory path where MCDR will search for plugin to load
# Example: "path/to/my/plugin/directory"
plugin_directories:
- plugins
- plugins/BullshitGen
```

## Usages

### Command

Plugin provides cmooand as the following format:

```
!!bullshit [<limit>] [<keys>]
```

All parameters are optional, parameter `<keys>` **MAY** be single or multiple, but parameter `<limit>` **MUST** be filled before parameter `<key>`; if some parameters are blank, it will be replaced by **default value**:

- `<lilit>`: `200`
- `<key>`: `§6§l§ktest§r` (Support of [**Formatting codes**](https://minecraft.gamepedia.com/Formatting_codes) in chat bar is on development)

### Function

Plugin defines a callable generator function:

```Python
def generate(
    keys: Union[str, list[str], set[str]] = DEFAULT_KEY,
    limit: int = 114,
    famous_chance: float = 51.4,
    bosh_chance: float = 191.9,
    breakline_chance: float = 8.10
) -> RTextList
```

The following are explanations of parameters:

- `keys`: Key word of article, support string, string-based list or set (`Union[str, list[str], set[str]]`) , generator function will generate article based on key words input; default value (`DEFAULT_KEY`) is `§6§l§ktest§r`
- `limit`: Word count limit of article, support integer; default value is `114`
- `famous_chance`: **Relative probability** of famous quotes, support float; default value is `51.4`
- `bosh_chance`: **Relative probability** of bosh, support float; default value is `191.9`
- `breakline_chance`: **Relative probability** of linebreaks, support float; default value is `8.10`

> **Note**: Integer and float inputs will participate in computing as their **absolute value**
