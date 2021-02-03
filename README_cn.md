# BullshitGen

[English](README.md) | **中文**

> **注意**：BullshitGen 基于 [**MCDR v1.x**](https://github.com/Fallen-Breath/MCDReforged) 开发，并且**不支持** MCDR v0.x

**BullshitGen** 是一个 MCDR 插件，移植了 [menzi11](https://github.com/menzi11)/[**BullshitGenerator**](https://github.com/menzi11/BullshitGenerator) 的代码和数据到 MCDR 平台，提供在聊天框中生成一段可复制、可自定义字数和关键词的**狗屁不通文章**生成器命令 `!!bullshit`，以及可被其他插件调用的自定义**狗屁不通文章**生成器函数 `generate()`。

## 安装插件

### 最新发布

在 [**Releases 页面**](https://github.com/Van-Involution/BullshitGen/releases)下载最新的 `BullshitGen.zip`，解压后将 `BullshitGen.py` 放入 `plugins/` 目录中，将 `BullshitData.json` 放入 `config/` 目录中。

### 最新源码

将仓库克隆（`git clone`）至 `plugins/` 目录中，复制一份 `BullshitData.json` 放入 `config/` 目录中，并按如下代码块编辑 **MCDR 实例**的 `config.yml`：

```YAML
# The list of directory path where MCDR will search for plugin to load
# Example: "path/to/my/plugin/directory"
plugin_directories:
- plugins
- plugins/BullshitGen
```

## 使用插件

### 命令

插件提供如下格式的命令：

```
!!bullshit [<字数>] [<关键词>]
```

所有参数均为可选，可以填入多个 `<关键词>` 参数，但在 `<关键词>` 参数前必须填入 `<字数>` 参数；若有未填参数，则使用**默认值**：

- `<字数>`：`200`
- `<关键词>`：`§6§l§ktest§r`（聊天框[**格式化代码**](https://minecraft-zh.gamepedia.com/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81)支持正在计划开发）

### 函数

插件定义了一个可供引用的生成器函数：

```Python
def generate(
    keys: Union[str, list[str], set[str]] = DEFAULT_KEY,
    limit: int = 114,
    famous_chance: float = 51.4,
    bosh_chance: float = 191.9,
    breakline_chance: float = 8.10
) -> RTextList
```

以下为参数含义：

- `keys`：文章的关键词，支持字符串、以字符串为元素的列表或集合（`Union[str, list[str], set[str]]`），生成器函数将根据输入的关键词生成文章；默认值（`DEFAULT_KEY`）为 `§6§l§ktest§r`
- `limit`：文章字数，支持整数；默认值为 `114`
- `famous_chance`：出现名人名言的**相对概率**，支持浮点数；默认值为 `51.4`
- `bosh_chance`：出现废话的**相对概率**，支持浮点数；默认值为 `191.9`
- `breakline_chance`：出现换行的**相对概率**，支持浮点数；默认值为 `8.10`

> **注意**：输入的整型或浮点参数会先取**绝对值**再参与运算
