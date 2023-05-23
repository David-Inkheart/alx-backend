# This project covers some concepts on i18n:
- How to parametrize Flask templates to display different languages
- How to infer the correct locale based on URL parameters, user   
    settings or request headers
- How to localize timestamps


# Tasks

### [0. Basic Flask app](./0-app.py)
* First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to my Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

### [1. Basic Babel setup](./1-app.py)
* Install the Babel Flask extension:
```
pip3 install flask_babel
```
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC")`.

Use that class as config for your Flask app.

### [2. Get locale from request](./2-app.py)
* Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

### [3. Parametrize templates](./3-app.py)
* Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file with the following content:
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

if the last line above throws an error, add a semicolon at the beginning of the line:
```
;extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with the following command:
```
pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with:
```
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
```
Finally, compile your dictionaries with:
```
Then edit the translations/en/LC_MESSAGES/messages.po and translations/fr/LC_MESSAGES/messages.po files to provide the correct value for each message ID. Use the following translations:
```
___________________________
| msgid | English | French |
|-------|---------|--------|
| `home_title` | `"Welcome to Holberton"` | `"Bienvenue chez Holberton"` |
| home_header | `"Hello world!"` | `"Bonjour monde!"` |
|-------|---------|--------|
___________________________

Then compile your dictionaries with:
```
pybabel compile -d translations
```

### [4. Force locale with URL parameter](./4-app.py)
In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

in your `get_locale` function, detect if the `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en].`

Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:

![image](https://user-images.githubusercontent.com/6486822/132944421-3b0b8b9a-0b0a-4b0a-9b0a-3b0b9a0b0a0b.png)

### [5. Mock logging in](./5-app.py)

### [6. Use user locale](./6-app.py)

### [7. Infer appropriate time zone](./7-app.py)

### [8. Display the current time](./app.py)