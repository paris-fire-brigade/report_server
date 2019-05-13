# app/views/general.py

from flask import Flask, request, url_for, redirect, Blueprint, render_template

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return render_template('general/index.html')

@mod.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('general.index'))

    # show the form, it wasn't submitted
    return render_template('general/cool_form.html')