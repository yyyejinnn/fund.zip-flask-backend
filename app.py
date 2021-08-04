from flask import Flask, render_template, session
#from flask_login import LoginManager, login_manager
from fund_views import user_view, analysis_view, fund_view


app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'  # 시크릿 키

app.register_blueprint(user_view.bp)  # 회원가입, 로그인
app.register_blueprint(analysis_view.bp)  # 투자성향
app.register_blueprint(fund_view.bp)  # 펀드 조회, 예측

#login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.session_protection = "strong"  # session 강화


@app.route("/", methods=['GET', 'POST'])
def index():
    if "userid" in session:
        return render_template(
            'main.html', username=session["userid"], login_result=True)
    else:
        return render_template('main.html', login_result=False)


if __name__ == '__main__':
    app.run(host="localhost", port="8082", debug=True)
