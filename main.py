# -*- coding: utf-8 -*-

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request, url_for, redirect
from flask.views import MethodView

from models import CourseRatings
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START index]
@app.route('/')
def index():
    return render_template('index.html')
# [END index]

# [START submissions]
@app.route('/submissions')
def submissions():
    submissions = CourseRatings.query()
    return render_template('submissions.html', submissions=submissions)
# [END submissions]


# [START form]
class FormHandler(MethodView):
    def get(self):
        """
        This renders the form page
        :return:
        """
        return render_template('form.html')

    def post(self):
        """
        This captures the form information.
        :return:
        """
        new_rating = CourseRatings()
        new_rating.email = request.form.get("email")
        new_rating.rating = int(request.form.get("rating"))
        new_rating.comments = request.form.get("comments")
        new_rating.put()
        return redirect(url_for('submissions'))
# [END form]

# [START error handler]
@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END error handler]

# [START add url rules]
app.add_url_rule('/form', view_func=FormHandler.as_view('form'))
# [END add url rules]

# [END app]
