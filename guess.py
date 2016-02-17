from flask import Flask, render_template, request, session, url_for
app = Flask(__name__)

app.secret_key = 'momomomomo'

@app.route('/')
def hello():
    return 'It works!'

@app.route('/guessmynumber/<name>/<int:answer>')
def guess(name, answer):
    correct = (answer == session.get('number'))

    return render_template(
        'guess.html',
        correct=correct
    )

@app.route('/register/', methods=['GET','POST'])
#@app.route('/register/<name>/<int:number>')
def register():
    name = request.form.get('name')
    number = request.form.get('number')
    if not name or not number:
        return render_template('register_page.html', error='Please enter your name and number!')
    #session = {'logged': True, 'user': name, 'number': number } # Why doesn't this work? XD
    session['logged'] = True
    session['user'] = name
    session['number'] = int(number)
    return render_template(
        'registered.html',
        user=name,
        number=number
    )

if __name__ == '__main__':
     # Our app will run on 127.0.0.1:5000 by default.
    app.run(debug=True)
