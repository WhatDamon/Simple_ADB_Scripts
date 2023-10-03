# 简易 ADB 脚本集

> [!WARNING]
> WIP, 无法保证稳定性!

一个无聊时开发的 ADB 脚本集工具，用于简化使用 ADB 来进行软件激活与安装的过程

## 文件简述

```
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
- [x] 下载 ADB
- [x] 通过 ADB 激活软件 (基本)
- [x] 通过 ADB 优化系统 (基本)
- [x] 通过 ADB 操作 Magisk (基本)
- [ ] 通过 ADB 安装软件

## 注意事项

1. 软件虽然对 macOS、Linux 有针对性开发, 但由于条件限制没法保证该程序可以在这两个平台能按照预期正常运行, 也请各位帮忙进行测试
2. 该程序最低支持 Python 3.5, 推荐使用 Python 3.9及更高版本运行该程序!

## 编译

以下指令最好在代码根目录下执行, 开始之前请确保使用到的 Python 版本不低于3.5!

### nuitka (推荐)

#### 编译前准备

请执行...

```bash
pip install nuitka
```

安装打包工具, 并提前安装好编译器 (Windows 下建议 MSVC, Linux 需要 GCC, macOS 可能需要 Xcode)

#### 编译指令

**1. MSVC**:

```bash
nuitka main.py --standalone --onefile --low-memory --enable-console --msvc=latest
```

**2. MinGW64**:

```bash
nuitka main.py --standalone --onefile --low-memory --enable-console --mingw64
```

**3. Clang**:

```bash
nuitka main.py --standalone --onefile --low-memory --enable-console --clang
```

### pyinstaller (简单)

#### 编译前准备

请执行...

```bash
pip install pyinstaller
```

安装打包工具, 不需要安装其他编译器

#### 编译指令

```bash
pyinstaller -F -c main.py
```

## 许可协议

```
MIT License

Copyright (c) 2023 Damon  Lu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```