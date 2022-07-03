
from flask import Flask, request

import api

app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'group':            # 如果是群聊信息
        Xingxi_id = request.get_json().get('message_id')                  # 信息ID
        Xingxi_text = request.get_json().get('raw_message')               # 信息内容
        QQ_name = request.get_json().get('sender').get('nickname')        # 发送者昵称
        QQ_id = request.get_json().get('sender').get('user_id')           # 发送者账号
        Qun_id = request.get_json().get('group_id')                       # 获取群号
        api.qunliao(Xingxi_id=Xingxi_id, Xingxi_text=Xingxi_text, QQ_name=QQ_name,QQ_id=QQ_id,Qun_id=Qun_id)  # 将 Q号和原始信息传到我们的后台

    # if request.get_json().get('message_type') == 'private':          # 如果是私聊信息
    #     QQ_name = request.get_json().get('sender').get('nickname')        # 发送者昵称
    #     QQ_id = request.get_json().get('sender').get('user_id')           # 发送者账号
    #     Xingxi_text = request.get_json().get('raw_message')               # 信息内容
    #     Xingxi_id = request.get_json().get('message_id')                  # 信息ID
    #     api.SiLiao(QQ_name=QQ_name, QQ_id=QQ_id,Xingxi_text=Xingxi_text,Xingxi_id=Xingxi_id)    # 将 Q号和原始信息传到我们的后台
    # if request.get_json().get('message_type') == 'guild':           # 频道消息
    #     Xingxi_id = request.get_json().get('message_id')
    #     Xingxi_text =request.get_json().get('message')
    #     ZhuPingDao_id = request.get_json().get('guild_id')
    #     ZiPingDao_id =request.get_json().get('channel_id')
    #     QQ_id = request.get_json().get('user_id')
    #     QQ_name = request.get_json().get('sender').get('nickname')
    #     api.zhanji(id=3,Xingxi_id=Xingxi_id, Xingxi_text=Xingxi_text, QQ_name=QQ_name,QQ_id=QQ_id,ZhuPingDao_id=ZhuPingDao_id,ZiPingDao_id=ZiPingDao_id)  # 将 Q号和原始信息传到我们的后台
    #
    # if request.get_json().get('notice_type') == 'group_decrease':            # 退群事件
    #     Qun_id = request.get_json().get('group_id')  # 获取群号
    #     QQ_id =  request.get_json().get('user_id')                  # 退群id
    #     CaoZhuo_id = request.get_json().get('operator_id')          # 操作者id
    #     Leixing = request.get_json().get('sub_type')                # 退群类型
    #     api.zhanji(id=4,QQ_id=QQ_id,CaoZhuo_id=CaoZhuo_id,Leixing=Leixing,Qun_id=Qun_id)
    #
    # if request.get_json().get('notice_type') == 'group_increase':            # 加群事件
    #     Qun_id = request.get_json().get('group_id')  # 获取群号
    #     CaoZhuo_id = request.get_json().get('operator_id')  # 操作者id
    #     QQ_id = request.get_json().get('user_id')    # 加群id
    #     api.zhanji(5,QQ_id=QQ_id,Qun_id=Qun_id,CaoZhuo_id=CaoZhuo_id)
    return 'OK'



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)  # 此处的 host和 port对应上面 yml文件的设置

