from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

# For the form

def write_to_file(data):
	with open("database.txt", "a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
	with open("database.csv",  "a", newline="") as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)	
		csv_writer.writerow([email, subject, message])	



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			# print(data['email'])	
			return redirect("thankyou.html")
		except:
			return "did not dave to database"	
	else:
		return "Something went wrong..Try again!"	
	

@app.route('/<string:page>')
def pages(page):
	# print("HIIIIIIII",page)
	return render_template(page)





# @app.route('/index.html')
# def index():
# 	return render_template('index.html')

# @app.route('/work.html')
# def work():
# 	return render_template('work.html')	

# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')			

# @app.route('/components.html')
# def components():
	return render_template('components.html')	