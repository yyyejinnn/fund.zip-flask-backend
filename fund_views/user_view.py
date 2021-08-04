from flask import Flask, Blueprint, request, flash, session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

from fund_controls.user_control import User

bp = Blueprint('user', __name__, url_prefix='/user')

# 회원가입


@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        ck_password = request.form['ck_password']
        name = request.form['name']

        # 1. Null값 확인
        if not(userid and password and ck_password and name):
            flash("빈칸을 채워주세요.")
            return redirect(url_for('user.signup'))

        else:  # 2. 중복 아이디 검사
            user = User.get(userid)
            if user != None:
                flash("아이디가 이미 존재합니다.")
                return redirect(url_for('user.signup'))
            else:
                pass

        # 3. 비밀번호 검사
        if (len(password) > 12) or (len(password) < 6):
            flash("비밀번호는 6자리이상 12자리 이하로 설정해주십시오.")
            return redirect(url_for('user.signup'))

        elif password != ck_password:
            flash("비밀번호가 일치하지 않습니다.")
            return redirect(url_for('user.signup'))

        else:  # 회원가입 성공
            User.signup(userid, password, name)
            flash("회원가입이 완료되었습니다.")
            return render_template('main.html')

    else:  # GET
        return render_template('user/signup.html')


# 로그인
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        session['userid'] = request.form['userid']
        return redirect(url_for('index'))
    return render_template('user/login.html')


# 로그아웃
@bp.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('index'))
