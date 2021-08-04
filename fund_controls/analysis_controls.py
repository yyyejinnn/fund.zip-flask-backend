from flask import Flask, session
from db_models import mysql


class Tendency():
    @staticmethod
    def updateTend(tendency):  # 투자성향 결과 DB 업데이트
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "UPDATE user_info SET analysis = '%s' where id = '%s'" % (
            str(tendency), session['userid'])
        cursor.execute(sql)
        conn.commit()

    @staticmethod
    def selectTend():  # 투자성향 마이페이지에 반영
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "SELECT analysis FROM user_info where id = '%s' " % session["userid"]

        cursor.execute(sql)
        user = cursor.fetchone()

        return user[0]  # analysis
