from flask import render_template, session, redirect, \
    url_for, current_app,request, send_file
from .. import db
from ..models import  Article
from . import main
from .forms import TryingForm


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/clock', methods=['GET', 'POST'])
def clock():
    return render_template('clock.html')

@main.route('/get_image', methods=['GET', 'POST'])
def get_image():
    filename = request.args.get('filename')
    print('here')
    if filename:
        print(filename)
        return send_file(f'static/{filename}')
    else:
        return False

@main.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    return render_template('bitcoin.html')\

@main.route('/globe', methods=['GET', 'POST'])
def globe():
    return render_template('globe.html')

@main.route('/watermark', methods=['GET', 'POST'])
def watermark():
    return render_template('watermark.html')

@main.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template('calendar.html')

@main.route('/monitor', methods=['GET', 'POST'])
def monitor():
    return render_template('monitor.html')

@main.route('/grid', methods=['GET', 'POST'])
def grid():
    return render_template('grid.html')

@main.route('/trying', methods=['GET', 'POST'])
def trying():
    form = TryingForm()
    if form.validate_on_submit():
        if form.exit.data:
            session['index'] = 0
            return redirect(url_for('main.index'))
        session['index'] = int(form.index.data)+1
        session['check'] = bool(form.check.data)
        return redirect(url_for('main.trying'))
    form.index.data = session.get('index')
    form.check.data = bool(session.get('check'))
    return render_template('trying.html', form=form)

