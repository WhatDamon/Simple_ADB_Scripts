# 导入模块
from os import system

# 变量初始化
AdbFullPath = None

# 设置 Adb 路径
def adbPathSet(path):
    global AdbFullPath
    AdbFullPath = '"' + path + '"'

# 设备列表
def adbDevicesList():
    print("\n为了保证软件正常运行, 请确保列表中只有一个设备!\n")
    system(AdbFullPath + ' devices')

# Shizuku 激活
def activeShizuku():
    print("\n激活命令来自于 Shizuku 软件内, 如有问题, 请联系 Shizuku 开发者或本软件开发者寻求更多信息!\n\n")
    system(AdbFullPath + ' shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh')
    print("\n")

# Dhizuku 激活
def activeDhizuku():
    print("\n激活命令来自于 Dhizuku 软件内, 如有问题, 请联系 Dhizuku 开发者或本软件开发者寻求更多信息!\n由于软件需要获取设备管理员权限, 如果无法运行, 请先退出“小米账号”、“华为账号”、“百度账号”等其他账号, 然后再试!\n")
    system(AdbFullPath + ' shell dpm set-device-owner com.rosan.dhizuku/.server.DhizukuDAReceiver')
    print("\n")

# 黑域应用内提供方式激活
def activeBreventS1():
    print("\n激活命令来自于黑域软件内, 如有问题, 请联系黑域的开发者或本软件开发者寻求更多信息!")
    system(AdbFullPath + ' shell sh /data/data/me.piebridge.brevent/brevent.sh')
    print("\n")

# 黑域官网提供方式激活
def activeBreventS2():
    print("\n激活命令来自于 https://brevent.sh/, 如有问题, 请联系黑域的开发者或本软件开发者寻求更多信息!")
    system(AdbFullPath + " -d shell 'output=$(pm path me.piebridge.brevent); export CLASSPATH=${output#*:}; app_process /system/bin me.piebridge.brevent.server.BreventServer bootstrap; /system/bin/sh /data/local/tmp/brevent.sh'")
    print("\n")

# Ice Box 激活
def activeIceBox():
    print("\n激活命令来自于 https://iceboxdoc.catchingnow.com/, 如有问题, 请联系冰箱的开发者或本软件开发者寻求更多信息!\n\n")
    system(AdbFullPath + ' shell sh /sdcard/Android/data/com.catchingnow.icebox/files/start.sh')
    print("\n")

# 小黑屋麦克斯韦妖模式激活
def activeBlackHouseS1():
    print("\n激活命令来自于 https://adb.http.gs/, 如有问题, 请联系小黑屋的开发者或本软件开发者寻求更多信息!")
    system(AdbFullPath + ' shell sh /sdcard/Android/data/web1n.stopapp/files/demon.sh')
    print("\n")

# 小黑屋设备管理员激活
def activeBlackHouseS2():
    print("\n激活命令来自于 https://adb.http.gs/, 如有问题, 请联系小黑屋的开发者或本软件开发者寻求更多信息!\n由于软件需要获取设备管理员权限, 如果无法运行, 请先退出“小米账号”、“华为账号”、“百度账号”等其他账号, 然后再试!\n")
    system(AdbFullPath + ' shell dpm set-device-owner web1n.stopapp/.receiver.AdminReceiver')
    print("\n")

# Scene5激活
def activeScene5():
    print("\n激活命令来自于开发者, 加载指令为自行整理, 如有问题, 请联系 Scene5 的开发者或本软件开发者寻求更多信息!\n")
    print("正在传输脚本到“下载”目录......\n")
    system(AdbFullPath + ' push ./scripts/scene_adb_init.sh /storage/emulated/0/Downloads')
    print("正在运行脚本......\n")
    system(AdbFullPath + ' shell sh /storage/emulated/0/Download/scene_adb_init.sh')
    print("如果没有报错, 则代表完成了该操作, 脚本文件将会留在下载目录, 请自行删除\n\n")