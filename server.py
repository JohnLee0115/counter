from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def view_count():
    if 'counter' in session:
        print('key exists!')
        session['counter'] += 1
    else:
        print('key numboftimes does NOT exist')
        session['counter'] = 0

    return render_template('index.html')

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def add_two():
    session['counter'] += 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)