from flask import Flask
from flask_login import UserMixin
from db_models import mysql


class User():
    # 회원가입
    @staticmethod
    def get(userid):  # get user
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "SELECT * FROM user_info where id = '%s' " % userid
        cursor.execute(sql)
        user = cursor.fetchone()

        if not user:
            return None
        else:
            return user

    @staticmethod  # signup
    def signup(userid, password, name):
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "INSERT INTO user_info(id, password, name) VALUES ('%s', '%s', '%s')" % (
            str(userid), str(password), str(name))
        cursor.execute(sql)
        conn.commit()

    # 로그인
    # get user - login
