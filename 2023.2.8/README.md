# starry-bot
星辰开源机器人

---
# 2023.2.8版本启动方法
本版本要求
数据库使用MySQL
## 1：修改配置文件config.json
修改方法请参考config_解析对照文件
## 2：导入数据库结构
目前版本只有一个必备表（用于心跳检测对照）

数据库文件为starry.sql
## 3：安装python扩展库
需要的依赖库有
```
pymysql  json  requests  smtplib  email  time os  re  flask  xpinyin 
```
## 4： 启动端口监听程序
```python
python3 start.py
```
# 启动机器人主体go-cqhttp
程序存放于qqbat文件下
windows 系统直接双击运行 **go-cqhttp.bat** 程序
Linux系统请按照go-cqhttp服务（自行解决，网上一大堆），**请务必进入qqbat目录下运行**

# 启动机器人心跳监听程序
启动该程序建议让机器人正确处理几条消息后在运行，数据库没有缓存数据可能出现误报

**windows系统** **Linux系统**没有安装zabbix-agentd端并且允许127.0.0.1访问

```python
# 满足以上条件则以下内容需全部注释
 CPU_util = float(os.popen("zabbix_get -s 127.0.0.1 -p 10050 -k 'system.cpu.util'").read().split()[0])
 Memory_util = 100 - float(
     os.popen("zabbix_get -s 127.0.0.1 -p 10050 -k 'vm.memory.size[pavailable]'").read().split()[0])
 text = "CPU：{:.2f}内存：{:.2f}".format(CPU_util, Memory_util)
 a = extend.Go_Cqhttp_data()
 a.business_card(config_json.get("main_Qun_id"),config_json.get("rebot_id"), text)
```
启动方法
```python
python3 heartbeat_start.py
```

