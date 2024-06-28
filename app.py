from flask import Flask, render_template
from routes.home import home_page
from routes.grades import grades_page
from routes.courses import courses_page
from api_routes.grades import grades_api
from api_routes.courses import courses_api

app = Flask(__name__, static_folder='static', template_folder='templates')

app.register_blueprint(home_page)
app.register_blueprint(grades_page)
app.register_blueprint(courses_page)
app.register_blueprint(grades_api)
app.register_blueprint(courses_api)

print(app.url_map)

from werkzeug.exceptions import HTTPException

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("500.html", error_message=e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

