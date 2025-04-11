from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Homepage</title>
        </head>
        <body>
            <p>Hello, World!</p>
            <h1>I like Oluwatobiloba</h1>
            <h2>She's very stubborn but i like that too!</h2>
        </body>
        </html>
    """

@app.route("/omolola")
def rafael():
    return "<p>Rafael</p>"

@app.route("/username/<name>")
def username(name):
    return f"<p>Good day everyone, My name is {name}</p>"


# =============
# ==DECORATOR==
# Decorators are functions that modify the behavior of another function.
# They are often used to add functionality to existing functions in a clean and readable way.
# =============

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "<p>Goodbye</p>"



if __name__ == "__main__":
    app.run(debug=True, port=5000)





# how to run the flask app:
# $env:FLASK_APP = "file.py"
# flask run