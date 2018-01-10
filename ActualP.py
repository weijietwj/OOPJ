from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/home'))
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/profiling')
def profiling():
    return render_template('profiling.html')


if __name__ == '__main__':
    app.run()
