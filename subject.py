
from xpinyin import Pinyin

import json
import time

# 导入自定义扩展
import extend
import QunGuan

# 读取配置文件
with open("config.json") as open_config:
    config_json = json.load(open_config)

# 初始化类
pinyin = Pinyin()   # 拼音转换
cqhttp_data = extend.Go_Cqhttp_data()   # cqhttp数据获取接口
requests_data = extend.Go_Cqhttp_requests()  # 发信接口
MySQL = extend.MySQL()  # MySQL接口

# 程序启动时间戳
start = config_json.get("start_time")

# 消息监听区
def QunLiao(json_data):
    # json解析
    Xingxi_id = json_data.get('message_id')  # 信息ID
    Xingxi_text = json_data.get('raw_message')  # 信息内容
    QQ_name = json_data.get('sender').get('nickname')  # 发送者昵称
    QQ_id = json_data.get('sender').get('user_id')  # 发送者账号
    reception_id = json_data.get('self_id')         # 接收者
    time_data = json_data.get('time')   # 时间戳
    Qun_id = json_data.get('group_id')  # 获取群号
    # 记录保存配置
    if config_json.get("save_data") == "True":
        timea = time.localtime(int(time_data))
        datatime = time.strftime("%Y-%m-%d %H:%M:%S", timea)
        SQL = "insert into `data%s`(`name`,`qq_id`,`reception_id`,`data`,`message_id`,`time`) values('%s','%s','%s','%s','%s','%s')" % (Qun_id,QQ_name,QQ_id,reception_id,Xingxi_text,Xingxi_id,datatime)
        MySQL.Update(SQL)
    # 群管功能
    if config_json.get("Admin_function") == "True":
        admin_list = []
        # 判断普通管理员身份有管理权限
        if config_json.get("admin").get("User_admin") == "True":
            admin_list = cqhttp_data.admin_list(Qun_id)
        else:
            admin_list.append(cqhttp_data.root_user(Qun_id))
        if QQ_id in admin_list:
            print(admin_list)
            print(QQ_id)
            QunGuan.Admin(json_data)










