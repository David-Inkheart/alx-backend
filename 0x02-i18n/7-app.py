#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user(login_as: int) -> Union[dict, None]:
    """ Returns: user dict or None if ID cannot be found """
    if login_as and int(login_as) in users:
        return users[int(login_as)]
    return None


@app.before_request
def before_request():
    """ Before request handler to get user and set as global"""
    g.user = get_user(request.args.get('login_as'))


@babel.localeselector
def get_locale() -> str:
    """ get locale from request and return best match"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    header_locale = request.headers.get('locale')
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Alternative way to use babel.localeselector
# babel.init_app(app, locale_selector=get_locale)


@babel.timezoneselector
def get_timezone() -> str:
    """ get timezone from request and return"""
    try:
        if request.args.get('timezone'):
            timezone = request.args.get('timezone')
            pytz.timezone(timezone)
            return timezone
        if g.user:
            timezone = g.user.get('timezone')
            pytz.timezone(timezone)
            return timezone
    except pytz.exceptions.UnknownTimeZoneError:
        """
        except pytz.exceptions.UnknownTimeZoneError as e:
        print(f"{e} is not a valid zone")
        """
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


# Alternative way to use babel.timezoneselector
# babel.init_app(app, timezone_selector=get_timezone)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Returns: 7-index.html """
    return render_template('7-index.html')


if __name__ == '__main__':
    """ Main Function"""
    app.run()
