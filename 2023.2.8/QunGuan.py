import json
import re

# 群管插件
# 导入自定义包
import extend


# 初始化类
extend_data = extend.MySQL()

# 读取配置文件
with open("config.json") as open_config:
    config_json = json.load(open_config).get("admin")

def Admin(json_data):

    # json解析
    Xingxi_id = json_data.get('message_id')  # 信息ID
    Xingxi_text = json_data.get('raw_message')  # 信息内容
    QQ_name = json_data.get('sender').get('nickname')  # 发送者昵称
    QQ_id = json_data.get('sender').get('user_id')  # 发送者账号
    reception_id = json_data.get('self_id')         # 接收者
    time_data = json_data.get('time')   # 时间戳
    Qun_id = json_data.get('group_id')  # 获取群号

    # 判断违禁词功能
    if config_json.get("error_words") == "True":
        pass
    # 查询历史消息
    if config_json.get("Recent_news") == "True":
        re_rule = r"\[CQ:at,qq=\d+\] 最近\d+条"
        if re.search(re_rule, Xingxi_text) is not None:
            qq_id = Xingxi_text.split("qq=")[1].split("]")[0]
            data1 = Xingxi_text.split("最近")[1].split("条")[0]
            data = extend.data_with()
            data_tmp = data.history_values(Qun_id=Qun_id,QQ_id=qq_id,values=data1)
            tmp = extend.Go_Cqhttp_requests()
            tmp.QunLiao_requests(Qun_id,data_tmp)

    # 问答功能
    if config_json.get("WenDa") == "True":
        pass



