from flask import Flask, Blueprint, request, flash, session, render_template


bp = Blueprint('fund', __name__, url_prefix='/fund')


@bp.route('/search')
def search():
    return render_template('fund/fundsearch.html')
