import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='jdbctester',
    passwd='4002017',
    db='webmail',
    charset='utf8'
)


def conn_mysqldb():  # 재접속
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)
    return MYSQL_CONN
