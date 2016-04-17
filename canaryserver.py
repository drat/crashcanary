from secrets import SENDGRID_KEY
import sendgrid
sg = sendgrid.SendGridClient(SENDGRID_KEY)
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def main():
    return redirect('https://github.com/revan/crashcanary')

@app.route('/crash', methods=['POST'])
def crash():
    name = request.form['body'].split('"')[1]
    message = sendgrid.Mail()
    message.add_to(request.form['email'])
    message.set_from('deadbird@crashcanary.org')
    message.set_subject('CrashCanary alert in %s!' % name)
    message.set_text(request.form['body'])
    status, msg = sg.send(message)
    return msg

if __name__ == '__main__':
    app.run(debug=True)
