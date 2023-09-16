# 导入模块
import os, sys, platform, ctypes, actions

# 变量初始化
AdbFullPath = None
ApkPath = None
adbRunFlag = False

# 启动选择项
def mainPage():
    print("请选择: \n1. 查看设备列表\n2. 激活软件\n3. 安装软件\n4. 退出\n")
    choice = input("请输入选项对应数字并回车(1~4): ")
    global adbRunFlag
    if choice == "1":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
        actions.adbDevicesList()
        print("\n如果显示设备未认证, 请在先在手机内通过调试请求\n")
        mainPage()
    elif choice == "2":
        activeApps()
    elif choice == "3":
        mainPage()
    elif choice == "4":
        print("\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        mainPage()
    choice = None

# 激活软件描述
def activeAppsDescription():
    print("\n\033[34m软件激活\033[0m\n========================================\n请从以下列表中选择您希望激活的软件\n该软件无法保证目前使用的的激活指令是否可以正常使用\n如果发生报错, 请自行查找适用的指令激活相关软件\n")
    activeApps()

# 激活软件选择项
def activeApps():
    print("请选择: \n1. Shizuku\n2. Dhizuku\n3. 黑域 Brevent\n4. 冰箱 Ice Box\n5. 小黑屋\n6. Scene5\n7. 返回上级\n")
    choice = input("请输入选项对应数字并回车(1~7): ")
    global adbRunFlag
    if choice == "1":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
        actions.activeShizuku()
        activeApps()
    elif choice == "2":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
        actions.activeDhizuku()
        activeApps()
    elif choice == "3":
        breventCommandSelect()
        activeApps()
    elif choice == "4":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
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
    global adbRunFlag
    if choice == "1":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
        actions.activeBreventS1()
        activeApps()
    elif choice == "2":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
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
    global adbRunFlag
    if choice == "1":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
        actions.activeBlackHouseS1()
        activeApps()
    elif choice == "2":
        if adbRunFlag == False:
            os.system('"' + AdbFullPath + '" usb')
            adbRunFlag = True
        actions.activeBlackHouseS2()
        activeApps()
    elif choice == "3":
        activeApps()
    else:
        print("\n\033[31m输入的内容不合法, 请重新输入!\033[0m\n")
        blackHouseCommandSelect()
    choice = None

# Scene5 脚本存在检查
def sceneScriptCheck():
    if(platform.system() == 'Windows'):
        scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "\\scripts\\scene_adb_init.sh"
    else:
        scriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "/scripts/scene_adb_init.sh"
    if os.path.exists(scriptPath) == True:
        actions.activeScene5
    else:
        print("\033[31m错误: 找不到脚本文件\033[0m\n")

# 主页面
def mainPageDescription():
    print("\033[32m简易 ADB 脚本集\033[0m\n========================================\n本软件能够简化您通过 adb 来进行软件激活与安装的过程,\n软件正在开发当中, 目前为止有很多软件还不能通过本软件进行激活,\n软件可能还会存在一些严重的 BUG 需要后期修复!\n建议在激活或者安装软件前使用第一项功能验证是否成功连接上您的设备.\n\033[33m注意: 目前只支持 USB 调试模式! 使用该软件前请确保设备可以被识别\033[0m\n版本: 1.0.0\n")
    print("\033[34mADB 主程序: \033[0m", AdbFullPath, "\n")
    mainPage()

# 启动脚本 & adb 存在检测
def start():
    global AdbFullPath
    AdbPath = None

    if(platform.system() == 'Windows'):
        AdbPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "\\bin"
        AdbFullPath = AdbPath + "\\adb.exe"
        ctypes.windll.kernel32.SetConsoleTitleW("简易 ADB 脚本集")
    else:
        AdbPath = os.path.split(os.path.realpath(sys.argv[0]))[0] + "/bin"
        AdbFullPath = AdbPath + "/adb"
    
    if os.path.exists(AdbFullPath) == True:
        actions.adbPathSet(AdbFullPath)
        mainPageDescription()
    else:
        print("\033[31m错误: 未找到 ADB, 正在退出......\033[0m\n")

# 从这里开始执行
if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print("\n\n\033[34m正在退出......\033[0m\n")
        if adbRunFlag == True:
            os.system('"' + AdbFullPath + '" kill-server')
        exit()
