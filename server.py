from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")  # decorator @app gives extra tool to build a server
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")  # decorator @app gives extra tool to build a server
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # write_to_file(data)
            # print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not saved to database'
    else:
        return 'something went wrong. Try again!'

# @app.route("/about.html")  # decorator @app gives extra tool to build a server
# def about():
#     return render_template('about.html')
#
#
# @app.route("/works.html")  # decorator @app gives extra tool to build a server
# def work():
#     return render_template('works.html')
#
#
# @app.route("/contact.html")  # decorator @app gives extra tool to build a server
# def contact():
#     return render_template('contact.html')
