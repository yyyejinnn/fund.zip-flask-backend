from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_manager, login_required, login_user, logout_user
from flask_cors import CORS
from fund_views import user_view


app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'  # 시크릿 키

app.register_blueprint(user_view.bp)  # 회원가입, 로그인

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"  # session 강화


@login_manager.unauthorized_handler  # 사용자 로그인 상태 확인
def unauthoerized():
    return make_response(jsonify(success=False), 401)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host="localhost", port="8082", debug=True)
