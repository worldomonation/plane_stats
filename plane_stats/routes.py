import pandas

from flask import render_template

from plane_stats import app
from plane_stats.fleet import get_airlines

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fleet')
def fleet():
    airlines = get_airlines()
    return render_template('public/fleet.html',
                           data=airlines.to_html(table_id="table-fleet", index=False))