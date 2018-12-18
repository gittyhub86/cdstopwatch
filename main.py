from flask import Flask, render_template, request
from datetime import datetime, timedelta
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/servertime/<string:offset>/')
def getTime(offset):
  serverTime = datetime.utcnow() - timedelta(hours=int(offset))
  return str(serverTime)

@app.route('/')
def main():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404