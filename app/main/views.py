from flask import render_template, session, redirect, url_for, current_app,request
from .. import db
from ..models import  Article
from . import main
from .forms import TryingForm


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


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

