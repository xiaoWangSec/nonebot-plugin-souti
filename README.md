<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://s3.bmp.ovh/imgs/2023/09/01/7d14c9c169c55535.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
</div>

<div align="center">

# nonebot-plugin-souti

_✨ 基于 Nonebot2 的一款文字搜题插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MPL2.0-blue" alt="license">
</a>
 <a href="https://pypi.org/project/nonebot-plugin-souti/">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-souti.svg" alt="pypi">
</a> 
<img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="python">


</div>


## 📖 介绍

基于 Nonebot2 的一款文字搜题插件, 使用百度不挂科题库

## 💿 安装

### 使用 nb-cli 安装
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-souti


### 使用包管理器安装
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

    pip install nonebot-plugin-souti


打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_souti"]


## 🎉 使用
### 指令表
| 指令 |  需要@ | 说明 |
|:-----:|:----:|:----:|
| 搜题 题目内容|  否 | 搜题命令, 后面带题目内容 |

### 效果图
![](https://s3.bmp.ovh/imgs/2023/09/01/6ff145ef497ade02.png)
