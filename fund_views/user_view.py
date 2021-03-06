from flask import Flask, Blueprint, request, flash, session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from fund_controls.user_control import User
from fund_controls.analysis_controls import Tendency
import bcrypt


# import functools

bp = Blueprint("user", __name__, url_prefix="/user")

# 회원가입
@bp.route("/signup", methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        signup_id = request.form["signup_id"]
        signup_pw = request.form["signup_pw"]
        ck_pw = request.form["ck_pw"]
        name = request.form["name"]

        # 1. Null값 확인
        if not (signup_id and signup_pw and ck_pw and name):
            flash("빈칸을 채워주세요.")
            return redirect(url_for("user.signup"))

        else:  # 2. 중복 아이디 검사
            user = User.get(signup_id)
            if user != None:
                flash("아이디가 이미 존재합니다.")
                return redirect(url_for("user.signup"))
            else:
                pass

        # 3. 비밀번호 검사
        if (len(signup_pw) > 12) or (len(signup_pw) < 6):
            flash("비밀번호는 6자리이상 12자리 이하로 설정해주십시오.")
            return redirect(url_for("user.signup"))

        elif signup_pw != ck_pw:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for("user.signup"))

        else:  # 회원가입 성공
            User.signUp(signup_id, signup_pw, name)
            flash("회원가입이 완료되었습니다.")
            return render_template("main.html")

    else:  # GET
        return render_template("user/signup.html")


# 로그인
@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        login_id = request.form["login_id"]
        login_pw = str(request.form["login_pw"])

        user = User.getUser(login_id)

        print(bcrypt.checkpw(login_pw.encode("utf-8"), user[1].encode("utf-8")))

        if user == None:  # 아이디가 존재하지 않으면
            flash("아이디를 확인해 주십시오.")
            return redirect(url_for("user.login"))
        elif not bcrypt.checkpw(login_pw.encode("utf-8"), user[1].encode("utf-8")):
            # user[1]: password,
            flash("비밀번호를 다시 확인해주십시오.")
            return redirect(url_for("user.login"))
        else:
            session["userid"] = login_id  # session값 저장
            return redirect(url_for("index"))

    else:  # GET
        return render_template("user/login.html")


# 로그아웃
@bp.route("/logout")
def logout():
    session.pop("userid", None)
    return redirect(url_for("index"))


# 마이페이지
@bp.route("/mypage")
def mypage():
    tendency = Tendency.selectTend()

    if tendency == None:
        user_tend = "-"
    else:
        user_tend = tendency

    return render_template("user/mypage.html", user_tend=user_tend)


# 비밀번호 변경
@bp.route("/editPw", methods=("GET", "POST"))
def editPw():
    if request.method == "POST":
        user_id = request.form["user_id"]
        edit_pw = request.form["edit_pw"]
        ck_pw = request.form["ck_pw"]

        # 1. Null값 확인
        if not edit_pw:
            flash("변경할 비밀번호를 입력해주십시오.")
            return redirect(url_for("user.mypage"))

        # 2. 비밀번호 검사
        if (len(edit_pw) > 12) or (len(edit_pw) < 6):
            flash("비밀번호는 6자리이상 12자리 이하로 설정해주십시오.")
            return redirect(url_for("user.mypage"))

        elif edit_pw != ck_pw:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for("user.mypage"))

        else:
            User.editPw(user_id, edit_pw)
            flash("비밀번호가 변경되었습니다. 다시 로그인 해주십시오")
            return redirect(url_for("user.logout"))


# 회원 탈퇴
@bp.route("/deleteUser", methods=("GET", "POST"))
def deleteUser():
    if request.method == "POST":
        user_id = request.form["user_id"]
        User.deleteUser(user_id)
        flash("탈퇴가 완료되었습니다.")
        return redirect(url_for("user.logout"))
