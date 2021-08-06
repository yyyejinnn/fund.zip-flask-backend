from flask import Flask, Blueprint, request, render_template, flash, redirect, session
from flask.helpers import url_for
from fund_controls.analysis_controls import Tendency

#from app import login_required

bp = Blueprint('analysis', __name__, url_prefix='/analysis')


@bp.route('/anahome', methods=('GET', 'POST'))
def anahome():
    return render_template('analysis/analysis.html')


@bp.route('/analysis', methods=('GET', 'POST'))  # 투자성향진단
def analysis():
    if request.method == 'POST':
        answer1 = float(request.form['answer1'])
        answer2 = float(request.form['answer2'])
        answer3 = float(request.form['answer3'])
        answer4 = float(request.form['answer4'])
        answer5 = float(request.form['answer5'])
        answer6 = float(request.form['answer6'])
        answer7 = float(request.form['answer7'])

        cal = answer1 + answer2 + answer3 + answer4 + answer5 + answer6 + answer7

        if cal <= 20:
            tendency = '안정형'
        elif cal > 20 and cal <= 40:
            tendency = '안정추구형'
        elif cal > 40 and cal <= 60:
            tendency = '위험중립형'
        elif cal > 60 and cal <= 80:
            tendency = '적극투자형'
        elif cal > 80:
            tendency = '공격투자형'

        Tendency.updateTend(tendency)  # 결과 DB에 업데이트
        # 펀드 추천 페이지로 넘어가기
        return render_template('analysis/result.html', tendency=tendency)

    else:  # GET
        if "userid" in session:  # 1. 로그인 되어있고
            user = Tendency.selectTend()
            if user:  # 1-1.만약 투자성향진단 결과가 이미 존재하면
                tendency = user
                return render_template('analysis/result.html', tendency=tendency)
            else:  # 1-2.투자성향진단 결과 존재하지 않으면
                return redirect(url_for('analysis.anahome'))

        else:  # 2. 로그인 안되어있으면
            flash('로그인이 필요한 서비스입니다.')
            return render_template("main.html")


@bp.route('/resultTend', methods=('GET', 'POST'))
def resultTend():
    if request.method == 'POST':
        correct = request.form['correct']

        if correct == '안정형':
            result = 5
        elif correct == '안정추구형':
            result = 4
        elif correct == '위험중립형':
            result = 3
        elif correct == '적극투자형':
            result = 2
        elif correct == '공격투자형':
            result = 1

        return render_template('analysis/ana_result.html', result=result)
