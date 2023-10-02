# 简易 ADB 脚本集

> [!WARNING]
> ⚠️ WIP, 无法保证稳定性!

一个无聊时开发的 ADB 脚本集工具，用于简化使用 ADB 来进行软件激活与安装的过程

## 文件简述

```Python
Simple_ADB_Scripts
 ├─ .vscode # VSCode 配置
 |   └─ settings.json
 ├─ scripts # 用于执行的脚本文件夹
 |   └─ scene_adb_init.sh # Scene5 激活脚本
 ├─ .gitattributes
 ├─ actions.py # 激活操作程序源码
 ├─ LICENSE # 使用 MIT 协议开源
 ├─ main.py # 主程序源码
 └─ README.md

```

##  TODO

- [x] 主要界面
- [x] 通过 ADB 激活软件 (基本)
- [x] 下载 ADB
- [ ] 通过 ADB 安装软件

## 注意事项

1. 软件虽然正对 macOS、Linux有针对性开发, 但由于一定的条件限制没法保证该程序可以在这两个平台正常运行, 也请各位帮忙进行测试
2. 该程序最低支持 Python 3.5, 推荐使用 Python 3.9及更高版本运行该程序!