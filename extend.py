# 星辰机器人三方外置扩展库
import pymysql
import json
import requests
import smtplib
from email.header import Header
from email.mime.text import MIMEText


# 读取配置文件
with open("config.json") as open_config:
    config_json = json.load(open_config).get("subject")

# 数据库接口
class MySQL:
    def Select(self,sql): # 数据表查询
        # 初始化连接对象
        mysqldb = pymysql.connect(host=config_json.get("MySQL_host"), user=config_json.get("MySQL_user"), password=config_json.get("MySQL_Pass"),
                                  database=config_json.get("MySQL_Database"), port=config_json.get("MySQL_post"))
        cursour = mysqldb.cursor()
        cursour.execute(sql)
        data = cursour.fetchall()
        mysqldb.close()
        return data

    # 数据库更新
    def Update(self,sql): # 数据表更新
        mysqldb = pymysql.connect(host=config_json.get("MySQL_host"), user=config_json.get("MySQL_user"), password=config_json.get("MySQL_Pass"),
                                  database=config_json.get("MySQL_Database"), port=config_json.get("MySQL_post"))
        cursour = mysqldb.cursor()
        cursour.execute(sql)
        mysqldb.commit()
        mysqldb.close()

# 发信接口
class Go_Cqhttp_requests:
    def SiLiao_requests(self,QQ_id,message):
        # 私聊提交接口
        # 127.0.0.1:5700/send_private_msg?user_id=qq号&message=消息
        destination = "send_private_msg"
        requests_url = "http://%s/%s" % (config_json.get("go-cqhttp_url"),destination)
        data = {
            "user_id":"%s" % QQ_id,
            "message":"%s" % message
        }
        requests.post(requests_url,data=data)

    def QunLiao_requests(self,Qun_id,message):
        # 群聊提交接口
        destination = "send_group_msg"
        requests_url = "http://%s/%s" % (config_json.get("go-cqhttp_url"),destination)
        data = {
            "group_id":"%s" % Qun_id,
            "message":"%s" % message
        }
        requests.post(requests_url,data=data)
    def PinDao_requests(self,Zu_id,Zi_id,message):
        # 频道提交接口
        destination = "end_guild_channel_msg"
        requests_url = "http://%s/%s" % (config_json.get("go-cqhttp_url"),destination)
        data = {
            "guild_id":"%s" % Zu_id,
            "channel_id":"%s"% Zi_id,
            "message":"%s" % message
        }
        requests.post(requests_url,data=data)


# 交互go-cqhttp获取数据
class Go_Cqhttp_data:
    # 获取群管理员列表
    def admin_list(self,Qun_id):
        destination = "get_group_member_list"
        requests_url = "http://%s/%s" % (config_json.get("go-cqhttp_url"), destination)
        data = {
            "group_id":"%s" % Qun_id
        }
        data_list = requests.post(requests_url,data=data).json().get("data")
        admin_list = []
        for i in data_list:
            if i.get("role") == "owner":
                admin_list.append(i.get("user_id"))
        return admin_list
    # 获取群主id
    def root_user(self,Qun_id):
        destination = "get_group_member_list"
        requests_url = "http://%s/%s" % (config_json.get("go-cqhttp_url"), destination)
        data = {
            "group_id":"%s" % Qun_id
        }
        return_data = requests.post(requests_url,data=data).json().get("data")
        admin = ""
        for i in return_data:
            if i.get("role") == "owner":
                admin = i.get("user_id")
        return admin
    # 修改群名片
    def business_card(self,Qun_id,QQ_id,name):
        destination = "set_group_card"
        requests_url = "http://%s/%s" % (config_json.get("go-cqhttp_url"), destination)
        data = {
            "group_id":"%s" % Qun_id,
            "user_id":"%s" % QQ_id,
            "card":"%s" % name

        }
        requests.post(requests_url,data=data).json().get("data")

# 自定义数据处理接口
class data_with:
    def history_values(self,Qun_id,QQ_id,values):
        sql = "SELECT * FROM (SELECT * FROM `data%s` WHERE `qq_id` = '%s' ORDER BY `id` DESC LIMIT %s )a ORDER BY `id`" % (Qun_id,QQ_id,values)
        select = MySQL()
        data = select.Select(sql)
        data_text = ""
        for i in data:
            tmp = """发件人：%s   发送时间%s
发送内容：%s\n\n""" % (i[1],i[6],i[4])
            data_text += tmp
        return data_text



# 邮件模块
class emil:
    def send(self,recipient,theme,data):
        smtp_server = "smtp.163.com"
        smtp_port = 465
        smtp_key = "FXNYGNZXXMIMLDVF"
        smtp_sender = "starry_one@163.com"  # 这里填入实际的发送端
        smtp_receiver = recipient  # 这里填入实际的接收端
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        smtp.login(smtp_sender, smtp_key)
        message = MIMEText(data, 'plain', 'utf-8')  # 发送的内容
        message['From'] = Header("starry系统邮件", 'utf-8')  # 发件人
        message['To'] = Header("管理员", 'utf-8')  # 收件人
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = theme  # 邮件标题
        smtp.sendmail(smtp_sender, smtp_receiver, message.as_string())
        smtp.close()


a = Go_Cqhttp_data()
a.business_card(953026557,3276394070,"名称测试")
