from flask import Flask, Blueprint, request, render_template, flash, redirect
from flask.helpers import url_for
from fund_controls.analysis_controls import Tendency

bp = Blueprint('analysis', __name__, url_prefix='/analysis')


@bp.route('/analysis', methods=('GET', 'POST'))
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

        Tendency.updateTend(tendency)
        return render_template('analysis/result.html', tendency=tendency)

    else:  # GET
        return render_template('analysis/analysis.html')


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
