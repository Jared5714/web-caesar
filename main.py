from flask import Flask, request
from caesar import encrypt

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
            <form method = "POST">
                <label for = "rot">Rotate by:
                <input name = "rot" type = "text" value = "0">
                </label>
                <br>
                <textarea name = "text" type = "textarea">{0}</textarea>
                <br>
                <input type = "submit" value = "Submit Query">
            </form>
        </body>

</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrpyt():
    text = request.form['text']
    rot = int(request.form['rot'])
    encrypt_mess = encrypt(text, rot)
    return form.format(encrypt_mess)

app.run()