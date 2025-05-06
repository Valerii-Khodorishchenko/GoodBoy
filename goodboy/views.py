from flask import render_template

from . import app, db
from .forms import ActivityForm
from .models import Activity


@app.route('/', methods=['GET', 'POST'])
def create_activity():
    print(1)
    form = ActivityForm()
    if not form.validate_on_submit():
        print(2)
        return render_template('activity_form.html', form=form)
    print(1)
    activity = Activity(name=form.name.data, description=form.description.data)
    db.session.add(activity)
    db.session.commit()
    return render_template('activity_form.html', form=form)
