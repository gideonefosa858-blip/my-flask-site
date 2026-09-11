print("Starting the app...")
import os

from flask import Flask, render_template, request
import json

app = Flask(__name__)

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

@app.route('/contacts')
def contacts_page():
    contacts = load_contacts()
    return render_template('contacts_list.html', contacts=contacts)

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