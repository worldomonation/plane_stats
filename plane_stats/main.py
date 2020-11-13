from flask import Flask, render_template

import pandas

from .fleet import get_airlines

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/fleet')
def fleet():
    airlines = get_airlines()
    return render_template('fleet.html',
                           tables=[airlines.to_html(index=False, 
                                                    classes='table')]
                          )
    # return render_template('fleet.html',
    #                        columns=airlines.columns,
    #                        data=airlines.to_json(orient='index'))
                        #    headers=['name', 'code', 'fleet size'],
                        #    objects=get_airlines())