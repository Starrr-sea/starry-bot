# 监听心跳，心跳停止则邮件警告
import time
import extend
import os
while True:
    # 读取当前心跳
    MySQL = extend.MySQL()
    hear = MySQL.Select("SELECT `value` FROM `tmp` WHERE `key` = 'heartbeat'")
    # 时间大于30分钟（1800）则警告
    if int(hear[0][0]) + 1800 < int(time.time()):
        # 实例化邮件接口
        emil = extend.emil()
        emil.send("2491267482","QQ机器人心跳警告","机器人停止运行，请立即排查问题")
        print("检测失败，当前时间戳%s" % time.time())
    else:
        CPU_util = float(os.popen("zabbix_get -s 127.0.0.1 -p 10050 -k 'system.cpu.util'").read().split()[0])
        Memory_util = 100 - float(
            os.popen("zabbix_get -s 127.0.0.1 -p 10050 -k 'vm.memory.size[pavailable]'").read().split()[0])
        text = "CPU：{:.2f}内存：{:.2f}".format(CPU_util, Memory_util)
        a = extend.Go_Cqhttp_data()
        a.business_card(542926457,3351593463, text)
        print("正常运行，当前时间戳%s" % time.time())
    time.sleep(120)