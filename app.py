from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Python', 'Flask']
    name = '30 days of Python programming'
    return render_template('home.html', techs = techs, name = name, title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8001))
    app.run(debug=True, host='0.0.0.0', port=port)