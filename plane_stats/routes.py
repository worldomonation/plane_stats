import pandas

from flask import Flask, render_template

from .fleet import get_airlines

from plane_stats import app

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/fleet')
def fleet():
    airlines = get_airlines()
    return render_template('public/fleet.html',
                           data=airlines.to_html(table_id="table-fleet", index=False))