from flask import Flask, Blueprint, request, flash, session, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os
#from fbprophet import Prophet

bp = Blueprint('fund', __name__, url_prefix='/fund')


@bp.route('/search')  # 펀드 조회
def search():
    return render_template('fund/fundsearch.html')


@bp.route('/predict', methods=('GET', 'POST'))  # 펀드 수익률 예측
def predict():
    '''
    if request.method == 'POST':  # post형식으로 가져오면
        value = request.form['num']  # num을 가져와서
        value = int(value)  # int로 형변환한다.

        # fund_번호 로 이루어진 형태이므로 입력한 값에 따라 다른 값을 읽는다.
        df = pd.read_csv('/static/fund/fund_%d.csv' % value)
        df = df[['date', 'rate']].dropna()  # 가로 date, 세로 rate
        df['date'] = pd.to_datetime(df['date'])  # 첫 열은 날짜이기 때문에 날짜 형태로
        df = df.set_index('date')
        daily_df = df.resample('d').mean()
        d_df = daily_df.reset_index().dropna()

        d_df.columns = ['ds', 'y']
        fig = plt.figure(facecolor='w', figsize=(20, 6))

        m = Prophet()  # 프로펫사용
        m.fit(d_df)
        future = m.make_future_dataframe(periods=500)  # 미래 500일까지 더 예측
        forecast = m.predict(future)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

        # 미래 예측
        from datetime import datetime, timedelta
        fig1 = m.plot(forecast)
        datenow = datetime.now()
        dateend = datenow + timedelta(days=100)
        datestart = dateend - timedelta(days=450)

        plt.xlim([datestart, dateend])
        plt.title("%d fund recommend" % value, fontsize=20)
        plt.xlabel("Day", fontsize=20)
        plt.ylabel("price", fontsize=20)
        plt.axvline(datenow, color="k", linestyle=":")
        plt.rcParams["figure.figsize"] = (7, 4)

        file = "/static/fund/fund.png"
        if os.path.isfile(file):  # 만약 이미 만들어진 fund.png있으면 삭제
            os.remove(file)
        plt.savefig('/static/fund/fund.png', bbox_inches='tight',
                    pad_inches=0)  # 무조건 plt.show이전에
'''
    return render_template('fund/predict.html')
