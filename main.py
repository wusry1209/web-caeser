from flask import Flask, request
from caeser import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">
        <label> Rotate by:
        <input value="0" type="text" name="rot">
        </label>
        <br>
        <label>
        <textarea name="text">{0}</textarea>
        </label>

        <input type="submit" value="Submit Query">
      </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    solution = rotate_string(request.form['text'], int(request.form['rot']))
    return form.format(solution)


@app.route("/")
def index():
    return form.format("")

app.run()