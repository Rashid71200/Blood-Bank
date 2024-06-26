from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('content.html', var_home = url_for('profiles'))

@app.route('/profile')
def profiles():
    return render_template('pagetwo.html')

@app.route('/feed')
def news_feed():
    return render_template('notification.html')

@app.route('/notification')
def notification():
    return render_template('news_feed.html')

@app.route('/page')
def page():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)
