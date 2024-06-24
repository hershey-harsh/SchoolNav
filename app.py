from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    return render_template("500.html", error_message=e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

