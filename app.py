print("Starting the app...")
import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['user_name']
        message = request.form['user_message']
        print(f"New message from {name}: {message}")
        return f"<h1>Thanks {name}, your message was received!</h1><a href='/'>Back to Home</a>"
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)