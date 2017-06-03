from flask import render_template

from . import weekly


@weekly.route('/winsun')
def winsun():
    return render_template('weekly/winsun.html')
