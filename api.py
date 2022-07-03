import time
import requests
import pymysql

# mysql定义区
sql_host = '121.40.178.171' # MySQL数据库连接地址
sql_database = 'qq_bat'     # 数据存放数据库，需要提前创建
sql_user = 'root'           # 数据库用户名
sql_pswword = '123456'      # 密码
sql_port = 3306             # 数据库端口

# 发信规则
SiLiao_URL = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'
QunLiao_URL = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'
PingDao_URL = 'http://127.0.0.1:5700/send_guild_channel_msg?guild_id={0}&channel_id={1}&message={2}'

# 运行时间
start = 1655084402
stop = int((int(time.time()) - start) / 60 / 60 / 24)


# 群聊
def qunliao(Xingxi_id=None, Xingxi_text=None, QQ_name=None, QQ_id=None, Qun_id=None, ZhuPingDao_id=None,
            ZiPingDao_id=None, CaoZhuo_id=None, Leixing=None):
    # 初始化系统问答
    date1 = {}
    date = SQL(key=2, sql="SELECT * FROM ADMIN")
    for i in date:
        date1[i[0]] = i[1]

    # 初始化管理员列表
    exec(date1.get("管理员列表"))
    admin.append(2491267482)  # 全局管理员

    # 全局参数问答
    # admin变量爆红不用管，该变量定义于数据库内部语句
    date2 = Xingxi_text.split()[0]
    if date1.get(date2) is not None:
        exec(date1.get(date2))


    # 判断群聊激活状态
    # 获取所有成功初始化的群
    date_tmp = SQL(key=2, sql="SHOW TABLES;")
    qunlist = []
    for i in date_tmp:
        qunlist.append(i[0])

    qun = str(Qun_id)
    quninfo = "%s_info" % Qun_id
    qunyaoqing = "%s_yaoqin" % Qun_id
    if qun in qunlist and quninfo in qunlist and qunyaoqing in qunlist:
        # 判断授权时间
        # 获取到期时间戳
        sql = "select `list` from %s_info where `name`=\"time\"" % Qun_id
        time_tmp = int(SQL(key=2, sql=sql)[0][0])
        time_info = int(time.time())
        if time_info > time_tmp:
            requests.get(QunLiao_URL.format(Qun_id, "已到期，请续费\n如有疑问请联系维护人员"))
        else:
            # 初始化群聊问答
            wenda = {}
            sql = "select * from `%s`" % Qun_id
            date = SQL(key=2, sql=sql)
            for i in date:
                wenda[i[0]] = i[1]

            # 自定义群聊回答
            if wenda.get(Xingxi_text) is not None:
                requests.get(QunLiao_URL.format(Qun_id, wenda.get(Xingxi_text)))
    else:
        requests.get(QunLiao_URL.format(Qun_id, "请进行群聊管理员进行初始化\n如果有问题请联系维护人员"))


# 退群事件
def tuiqun():
    pass


# 加群事件
def jiaqun():
    pass


# 数据库部分
def SQL(key=None, sql=None, Qun_id=None):
    # 初始化连接对象
    mysqldb = pymysql.connect(host=sql_host, user=sql_user, password=sql_pswword, database=sql_database, port=sql_port)
    cursour = mysqldb.cursor()
    try:
        # key 1  无返回值，插入操作
        # key 2  有返回值，查询操作
        # key 3  初始化建库操作
        if key == 1:
            cursour.execute(sql)
            # 提交修改语句
            mysqldb.commit()
        elif key == 2:
            cursour.execute(sql)
            data = cursour.fetchall()
            return data
        elif key == 3:
            # 自定义问答表
            cursour.execute(
                "CREATE TABLE `%s`( `Wen` VARCHAR(254) NULL, `Da` text, `QQ_id` bigint(254) NULL )" % Qun_id)

            # 邀请计数表
            cursour.execute("CREATE TABLE `%s_yaoqin`( `name` VARCHAR(254) NULL , `yaoqing` text )" % Qun_id)
            # 群聊信息表
            times = int(time.time()) + 260000
            cursour.execute("CREATE TABLE `%s_info`( `name` text , `list` text )" % Qun_id)

            cursour.execute(
                "INSERT INTO `%s`(`wen`,`da`) VALUES (\"维护人员\",\"联系方式2491267482\n邮箱：starry_@163.com\")" % Qun_id)
            cursour.execute("INSERT INTO `%s_info`(`name`,`list`) VALUES (\"time\",\"%s\")" % (Qun_id, times))
            mysqldb.commit()
    except:
        return False
    mysqldb.close()

# # 私聊
# def SiLiao(QQ_name=None, QQ_id=None, Xingxi_text=None, Xingxi_id=None):
#     if re.search(r'你是.*', Xingxi_text) != None:
#         text = "本人由星辰工作室开发\n目前开发人员只有一人\n已正常运行%s天\n加入团队请联系邮箱\nstarry_one@163.com\n服务器性能和资金原因，只对10个群提供功能\n后续在看，主要是钱包" % stop
#         requests.get(SiLiao_URL.format(QQ_id, text))
#
#
# # 频道
# def PingDao(Xingxi_id=None, Xingxi_text=None, QQ_name=None, QQ_id=None, ZhuPingDao_id=None, ZiPingDao_id=None):
#     if re.search(r'星辰', Xingxi_text) != None:
#         text = "本人由星辰工作室开发\n目前开发人员只有一人\n已正常运行%s天\n加入团队请联系邮箱\nstarry_one@163.com\n服务器性能和资金原因，只对10个群提供功能\n后续在看，主要是钱包" % stop
#         requests.get(PingDao_URL.format(ZhuPingDao_id, ZiPingDao_id, text))
#
