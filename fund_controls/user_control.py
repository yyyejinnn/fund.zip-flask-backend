from flask import Flask
from db_models import mysql
import bcrypt


class User:
    # 회원가입
    @staticmethod
    def get(signup_id):  # get user
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "SELECT * FROM user_info where id = '%s' " % signup_id
        cursor.execute(sql)
        user = cursor.fetchone()

        if not user:
            return None
        else:
            return user

    @staticmethod  # signup
    def signUp(signup_id, signup_pw, name):

        hash_pw = bcrypt.hashpw(str(signup_pw).encode("utf-8"), bcrypt.gensalt())
        save_pw = hash_pw.decode("utf-8")

        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "INSERT INTO user_info(id, password, name) VALUES ('%s', '%s', '%s')" % (
            str(signup_id),
            save_pw,
            str(name),
        )
        cursor.execute(sql)
        conn.commit()

    # 로그인
    @staticmethod
    def getUser(login_id):  # get user
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "SELECT * FROM user_info where id = '%s' " % login_id

        cursor.execute(sql)
        user = cursor.fetchone()

        if not user:
            return None
        else:
            return user

    # 비밀번호 변경
    @staticmethod
    def editPw(user_id, edit_pw):
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "UPDATE user_info SET password = '%s' where id = '%s'" % (
            str(edit_pw),
            str(user_id),
        )

        cursor.execute(sql)
        conn.commit()

    # 회원탈퇴
    @staticmethod
    def deleteUser(user_id):
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "DELETE FROM user_info where id = '%s' " % user_id

        cursor.execute(sql)
        conn.commit()
