from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['SET_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Python', 'Flask']
    name = '30 days of Python programming'
    return render_template('home.html', techs = techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 days of Python programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8001))
    app.run(debug=True, host='0.0.0.0', port=port)