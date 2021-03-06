from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('WELCOME TO EMAILWING!')

@app.route('/<from_user>/<email_id>/<approver>')
def server(from_user, email_id, approver):
  return render_template('index.html', \
      from_user=from_user.replace('.',','), email_id=email_id, approver=approver.replace('.',','))


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

