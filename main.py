# 导入模块
import os, sys, urllib.request, zipfile, time, actions
from platform import platform, machine
from pathlib import Path
from shutil import rmtree
from math import floor
from hashlib import md5

# ---------- #

# 变量初始化
AdbFullPath = None
ApkPath = None
adbRunFlag = False
adbDownloadFrom = None

# ---------- #

# 主页面
def mainPageDescription():
    print("\033[32m简易 ADB 脚本集\033[0m\n========================================\n本软件能够简化您通过 adb 来进行软件激活与安装的过程,\n软件正在开发当中, 目前为止有很多软件还不能通过本软件进行激活,\n软件可能还会存在一些严重的 BUG 需要后期修复!\n建议在激活或者安装软件前使用第一项功能验证是否成功连接上您的设备.\n\033[33m注意: 目前只支持 USB 调试模式! 使用该软件前请确保设备可以被识别, 搞机有风险, 请谨慎操作.\033[0m\n本软件使用 MIT 协议开源.\n版本: 1.0.0_commit7\n")
    print("\033[34mADB 主程序位置: \033[0m", AdbFullPath)
    print("\033[34m运行系统平台: \033[0m", platform(), "-", os.name, "-", sys.platform, "-", machine(), "\n", sep = '')
    mainPage() 

# 启动选择项
def mainPage():
    print("请选择: \n1. 查看设备列表\n2. 激活软件\n3. 安装 & 卸载软件\n4. 系统优化\n5. Magisk 操作\n6. 系统更新配置\n7. 重启手机\n8. 更多选项\n9. 退出\n")
    choice = input("请输入选项对应数字并回车(1~9): ")
    global adbRunFlag
    if choice == "1":
        checkAdbUsbConnect()
        actions.adbDevicesList()
        print("\n如果显示设备未认证, 请在先在手机内通过调试请求\n")
        mainPage()
    elif choice == "2":
        activeAppsDescription()
    elif choice == "3":
        print("\n\033[31m正在开发...\033[0m\n")
        mainPage()
    elif choice == "4":
        sysOptiDescription()
    elif choice == "5":
        magiskDescription()
    elif choice == "6":
        print("\n\033[31m正在开发...\033[0m\n")
        mainPage()
    elif choice == "7":
        rebootDescription()
    elif choice == "8":
        moreOptionsDescription()
    elif choice == "9":
        print("\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        mainPageDescription()
    choice = None

# 激活软件描述
def activeAppsDescription():
    print("\n\033[34m软件激活\033[0m\n========================================\n请从以下列表中选择您希望激活的软件\n该软件无法保证目前使用的的激活指令是否可以正常使用\n如果发生报错, 请自行查找适用的指令激活相关软件\n")
    activeApps()

# 激活软件选择项
def activeApps():
    print("请选择: \n1. Shizuku\n2. Dhizuku\n3. 黑域 Brevent\n4. 冰箱 Ice Box\n5. 小黑屋\n6. Scene5\n7. 返回上级\n")
    choice = input("请输入选项对应数字并回车(1~7): ")
    if choice == "1":
        checkAdbUsbConnect()
        actions.activeShizuku()
        activeApps()
    elif choice == "2":
        checkAdbUsbConnect()
        actions.activeDhizuku()
        activeApps()
    elif choice == "3":
        breventCommandSelect()
        activeApps()
    elif choice == "4":
        checkAdbUsbConnect()
        actions.activeIceBox()
        activeApps()
    elif choice == "5":
        blackHouseCommandSelect()
        activeApps()
    elif choice == "6":
        sceneScriptCheck()
        activeApps()
    elif choice == "7":
        mainPage()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        activeApps()
    choice = None

# 黑域指令选择
def breventCommandSelect():
    print("\n激活黑域有两种方式可选!\n\n请选择: \n1. 应用内提供方式\n2. 官网提供方式\n3. 放弃\n")
    choice = input("请输入选项对应数字并回车(1~3): ")
    if choice == "1":
        checkAdbUsbConnect()
        actions.activeBreventS1()
        activeApps()
    elif choice == "2":
        checkAdbUsbConnect()
        actions.activeBreventS2()
        activeApps()
    elif choice == "3":
        activeApps()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        breventCommandSelect()
    choice = None

# 小黑屋指令选择
def blackHouseCommandSelect():
    print("\n激活小黑屋有两种模式可选!\n\n请选择: \n1. 麦克斯韦妖模式\n2. 设备管理员模式\n3. 放弃\n")
    choice = input("请输入选项对应数字并回车(1~3): ")
    if choice == "1":
        checkAdbUsbConnect()
        actions.activeBlackHouseS1()
        activeApps()
    elif choice == "2":
        checkAdbUsbConnect()
        actions.activeBlackHouseS2()
        activeApps()
    elif choice == "3":
        activeApps()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        blackHouseCommandSelect()
    choice = None

# Scene5 脚本存在检查 & 校验
def sceneScriptCheck():
    scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "/scripts/scene_adb_init.sh"
    if os.path.exists(scriptPath) == True:
        with open(scriptPath, 'rb') as fp:
            data = fp.read()
        md5Data = md5(data).hexdigest()
        if md5Data == 'e6ab442856912d8af60d98be2126c0d3':
            actions.activeScene5()
        else:
            print("\n\033[31m错误: 文件校验失败\033[0m\n现有脚本文件 MD5 为:", md5Data, "\n为了您的设备安全, 停止执行, 如果原脚本已经失效, 请联系开发者或者向本项目仓库提交 PR 或 Issue!\n")
    else:
        print("\n\033[31m错误: 找不到脚本文件\033[0m\n")

# 检查 ADB USB 连接
def checkAdbUsbConnect():
    global adbRunFlag
    if adbRunFlag == False:
        os.system('"' + AdbFullPath + '" usb')
        adbRunFlag = True

# 系统优化描述
def sysOptiDescription():
    print("\n\033[34m系统优化\033[0m\n========================================\n请从以下列表中选择您希望优化的系统\n该软件无法保证目前使用的的指令是否可以正常使用\n\033[31m存在风险! 谨慎操作\033[0m\n")
    sysOpti()

# 系统优化选择项
def sysOpti():
    print("请选择: \n1. MIUI\n2. 返回上级\n")
    choice = input("请输入选项对应数字并回车(1~2): ")
    if choice == "1":
        miuiOptiCheck()
        sysOpti()
    elif choice == "2":
        mainPageDescription()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        sysOpti()
    choice = None

# MIUI系统优化前确定
def miuiOptiCheck():
    print("\n\033[33m警告:\033[0m\n操作不当可能会造成卡米、数据丢失等问题, 或者其他不可预料的后果!\n是否继续?\n\n\033[33m“y”代表“确定”,“N”代表“取消”,默认值为“N”\033[0m\n")
    choice = input("请选择(y/N): ")
    if choice == "y" or choice == "Y":
        checkAdbUsbConnect()
        actions.miuiOpti()
        sysOpti()
    elif choice == "N" or choice == "n" or choice == "":
        print("\n")
        sysOpti()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        choice = None
        miuiOptiCheck()

# Magisk 操作描述
def magiskDescription():
    print("\n\033[34mMagisk 操作\033[0m\n========================================\n请从以下列表中选择您希望进行的操作\n该软件无法保证目前使用的的指令是否可以正常使用\n\033[31m涉及内核, 存在风险! 谨慎操作\033[0m\n")
    magiskAction()

# Magisk 操作选择项
def magiskAction():
    print("请选择: \n1. 删除所有模块 (可用于救砖)\n2. 返回上级\n")
    choice = input("请输入选项对应数字并回车(1~2): ")
    if choice == "1":
        magiskDelModCheck()
        sysOpti()
    elif choice == "2":
        mainPageDescription()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        sysOpti()
    choice = None

# Magisk 删除模块前前确定
def magiskDelModCheck():
    print("\n\033[33m警告:\033[0m\n涉及系统内核, 操作不当可能会导致设备永久变砖, 或者其他不可预料的后果!\n是否继续?\n\n\033[33m“y”代表“确定”,“N”代表“取消”,默认值为“N”\033[0m\n")
    choice = input("请选择(y/N): ")
    if choice == "y" or choice == "Y":
        checkAdbUsbConnect()
        actions.magiskDelAllMod()
        magiskAction()
    elif choice == "N" or choice == "n" or choice == "":
        print("\n")
        magiskAction()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        choice = None
        magiskDelModCheck()

# 重启描述
def rebootDescription():
    print("\n\033[34m重启手机\033[0m\n========================================\n请从以下列表中选择您希望的手机重启方案\n")
    rebootPh()

# 重启手机选择项
def rebootPh():
    print("请选择: \n1. 普通重启\n2. 重启到 Recovery\n3. 重启到 Fastboot\n4. 重启到高通 EDL 紧急刷机模式 (9008)\n5. 返回上级\n")
    choice = input("请输入选项对应数字并回车(1~5): ")
    if choice == "1":
        rebootPhCheck(0)
        rebootPh()
    elif choice == "2":
        rebootPhCheck(1)
        rebootPh()
    elif choice == "3":
        rebootPhCheck(2)
        rebootPh()
    elif choice == "4":
        rebootPhCheck(3)
        rebootPh()
    elif choice == "5":
        mainPageDescription()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        rebootPh()
    choice = None

# 重启手机前优化前确定
def rebootPhCheck(way):
    print("\n请确保手机重启前已经保存了所有资料\n是否继续?\n\n\033[33m“y”代表“确定”,“N”代表“取消”,默认值为“N”\033[0m\n")
    choice = input("请选择(y/N): ")
    if choice == "y" or choice == "Y":
        checkAdbUsbConnect()
        actions.reboot(way)
        rebootPh()
    elif choice == "N" or choice == "n" or choice == "":
        print("\n")
        rebootPh()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        choice = None
        rebootPhCheck()
    way = None

# 更多选项描述
def moreOptionsDescription():
    print("\n\033[34m更多选项\033[0m\n========================================\n请从以下列表中选择您希望进行的操作\n")
    moreOptions()

# 重启手机选择项
def moreOptions():
    print("请选择: \n1. 查看 ADB 信息\n2. 重新下载 ADB\n3. 返回上级\n")
    choice = input("请输入选项对应数字并回车(1~5): ")
    if choice == "1":
        print("\n")
        actions.adbInfo()
        print("\n")
        moreOptions()
    elif choice == "2":
        rmtree(os.path.split(os.path.realpath(sys.argv[0]))[0] + "/platform-tools")
        adbDownloadFromChoose()
    elif choice == "5":
        mainPageDescription()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        moreOptions()
    choice = None

# ---------- #

# 确认是否自动下载 ADB
def downloadAdbOrNot():
    choice = input("请选择(y/N): ")
    if choice == "y" or choice == "Y":
        adbDownloadFromChoose()
    elif choice == "N" or choice == "n" or choice == "":
        print("\n\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        choice = None
        downloadAdbOrNot()

# 选择 ADB 下载来源
def adbDownloadFromChoose():
    print("\n请选择下载源:\n\n1. Google Developers International (适用于非中国大陆地区)\n2. 谷歌中国开发者平台 (适用于中国大陆地区)\n3. 退出\n")
    choice = input("请输入选项对应数字并回车(1~3): ")
    global adbDownloadFrom
    if choice == "1" or choice == "2":
        adbDownloadFrom = choice
        downloadAdb()
    elif choice == "3":
        print("\n\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        adbDownloadFromChoose()
    choice = None

# 下载 ADB
def downloadAdb():
    url = None
    # 检查网络连接
    def connectionCheck(web):
        try:
            urllib.request.urlopen(web, timeout = 10)
            print("\n")
            return True
        except urllib.error.URLError as e:
            print("\n无法连接到服务器!")
            return False
        
    # 检查并创建目录
    def dirCreate(dirName):
        dirPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "/" + dirName
        Path(dirPath).mkdir(parents = True, exist_ok = True)

    # 解压 ADB
    def unzipAdb(path):
        savePath = os.path.split(os.path.realpath(sys.argv[0]))[0]
        file = zipfile.ZipFile(path)
        print("\n\n正在解压...")
        file.extractall(savePath)
        file.close()

    # 下载进度条
    def schedule(blocknum, blocksize, totalsize):
        # 进度条输出
        def progressbar(cur, speedStr, total = 100):
            percent = '{:.2%}'.format(cur / total)
            sys.stdout.write('\r')
            sys.stdout.write("\033[32m[%-50s]\033[0m %s %s" % ('=' * int(floor(cur * 50 / total)), percent, speedStr))
            sys.stdout.flush()

        # 字节单位转化
        def formatSize(bytes):
            try:
                bytes = float(bytes)
                kb = bytes / 1024
            except:
                return "Unknow"
            if kb >= 1024:
                M = kb / 1024
                if M >= 1024:
                    G = M / 1024
                    return "%.1fGB/s" % (G)
                else:
                    return "%.1fMB/s" % (M)
            else:
                return "%.1fKB/s" % (kb)
        
        speed = (blocknum * blocksize) / (time.time() - startTime)
        speedStr = "%s" % formatSize(speed)
        if totalsize == 0:
            percent = 0
        else:
            percent = blocknum * blocksize / totalsize
        if percent > 1.0:
            percent = 1.0
        percent = percent * 100
        progressbar(percent, speedStr)
    
    # 下载前准备
    global adbDownloadFrom
    if adbDownloadFrom == "1":
        if sys.platform.startswith('win'):
            url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
        elif sys.platform.startswith("linux"):
            url = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
        elif sys.platform.startswith('darwin'):
            url = "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
        else:
            print("\n\033[31m错误: ADB 可能不支持您所使用的平台:\033[0m\n", platform(), "-", os.name, "-", sys.platform, "-", machine(), "\n\n\033[34m正在退出......\033[0m\n", sep = '')
            if adbRunFlag == True:
                os.system('"' + AdbFullPath + '" kill-server')
            exit()
    elif adbDownloadFrom == "2":
        if sys.platform.startswith('win'):
            url = "https://googledownloads.cn/android/repository/platform-tools-latest-windows.zip"
        elif sys.platform.startswith("linux"):
            url = "https://googledownloads.cn/android/repository/platform-tools-latest-linux.zip"
        elif sys.platform.startswith('darwin'):
            url = "https://googledownloads.cn/android/repository/platform-tools-latest-darwin.zip"
        else:
            print("\n\033[31m错误: ADB 可能不支持您所使用的平台:\033[0m\n", platform(), "-", os.name, "-", sys.platform, "-", machine(), "\n\n\033[34m正在退出......\033[0m\n", sep = '')
            if adbRunFlag == True:
                os.system('"' + AdbFullPath + '" kill-server')
            exit()
    
    # 下载阶段
    if connectionCheck(url) == True:
        dirCreate('tmp')
        try:
            downloadPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "/tmp/adb.zip"
            startTime = time.time()
            print("开始下载!")
            urllib.request.urlretrieve(url, downloadPath, schedule)
            unzipAdb(downloadPath)
            rmtree(os.path.split(os.path.realpath(sys.argv[0]))[0] + "/tmp")
            print("完成!\n")
            start()
        except Exception as e:
            print("\n\033[31m错误: 下载过程出现错误\033[0m\n\n\033[34m正在退出......\033[0m\n")
            if adbRunFlag == True:
                os.system('"' + AdbFullPath + '" kill-server')
            exit()
    else:
        print("\n\033[31m错误: 网络连接失败\033[0m\n\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()

# ---------- #

# 启动脚本 & ADB 存在检测
def start():
    global AdbFullPath
    AdbPath = None

    if sys.platform.startswith('win'):
        AdbPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "\\platform-tools"
        AdbFullPath = AdbPath + "\\adb.exe"
        from ctypes import windll
        windll.kernel32.SetConsoleTitleW("简易 ADB 脚本集")
    elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        AdbPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "/platform-tools"
        AdbFullPath = AdbPath + "/adb"
    else:
        print("\n\033[31m错误: 不支持您所使用的平台:\033[0m\n", platform(), "-", os.name, "-", sys.platform, "-", machine(), "\n\n\033[34m正在退出......\033[0m\n", sep = '')
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
    
    if os.path.exists(AdbFullPath) == True:
        actions.adbPathSet(AdbFullPath)
        mainPageDescription()
    else:
        print("\033[31m错误: 未找到 ADB\033[0m\n\n您可以考虑让软件为您下载 ADB\n请选择是否要这么做?\n\n\033[33m“y”代表“确定”,“N”代表“取消”,默认值为“N”\033[0m\n")
        downloadAdbOrNot()

# 从这里开始执行
if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print("\n\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
