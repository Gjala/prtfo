from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about_us():
    return render_template('about.html')

@app.route("/works")
def works_page():
    return render_template('works.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/components")
def components_page():
    return render_template('components.html')

@app.route("/thank_you")
def thanks():
    return render_template('thank_you.html')

#contact page obj data

def write_to_file(data):
    with open('db.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        date = datetime.now()
        file = database.write(f'\n email: {email},Subject: {subject}, Message: {message} {date}')

def write_to_csv(data):
    with open('db.csv', mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        date = datetime.now()
        csv_writer = csv.writer(database2,  delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message,date])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong . Try again'