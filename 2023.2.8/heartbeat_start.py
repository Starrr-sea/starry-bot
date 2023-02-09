# 监听心跳，心跳停止则邮件警告
import time
import extend
import os
import json

# 读取配置文件
with open("config.json") as open_config:
    config_json = json.load(open_config).get("hear")

while True:
    # 读取当前心跳
    MySQL = extend.MySQL()
    hear = MySQL.Select("SELECT `value` FROM `tmp` WHERE `key` = 'heartbeat'")
    time_data = int(time.time())
    timea = time.localtime(int(time_data))
    datatime = time.strftime("%Y-%m-%d %H:%M:%S", timea)
    # 时间大于30分钟（1800）则警告
    if int(hear[0][0]) + 1800 < time_data:
        # 实例化邮件接口
        emil = extend.emil()
        emil.send(config_json.get("main_admin"),"QQ机器人心跳警告","机器人停止运行，请立即排查问题")
        print("检测失败，当前时间%s" % datatime)
    else:
        CPU_util = float(os.popen("zabbix_get -s 127.0.0.1 -p 10050 -k 'system.cpu.util'").read().split()[0])
        Memory_util = 100 - float(
            os.popen("zabbix_get -s 127.0.0.1 -p 10050 -k 'vm.memory.size[pavailable]'").read().split()[0])
        text = "CPU：{:.2f}内存：{:.2f}".format(CPU_util, Memory_util)
        a = extend.Go_Cqhttp_data()
        a.business_card(config_json.get("main_Qun_id"),config_json.get("rebot_id"), text)
        print("正常运行，当前时间%s" % datatime)
    time.sleep(config_json.get("sleep"))