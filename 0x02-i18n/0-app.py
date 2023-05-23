#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/',  strict_slashes=False)
def index():
    """ Returns: 0-index.html """
    header = "Hello world"
    return render_template('0-index.html', header=header)
