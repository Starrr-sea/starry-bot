from flask import Flask, request
import subject
import extend

app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    json_data = request.get_json()
    # 群聊消息过滤
    if json_data.get('message_type') == 'group':            # 如果是群聊信息
        subject.QunLiao(json_data)
    # 心跳数据过滤
    elif json_data.get("post_type") == 'meta_event':        # 心跳检测
        MySQL = extend.MySQL()
        MySQL.Update("UPDATE `tmp` SET `value` = '%s' WHERE `key` = 'heartbeat'" % json_data.get("time"))
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5701,threaded=True)  # 此处的 host和 port对应上面 yml文件的设置,threaded=True开启多线程
