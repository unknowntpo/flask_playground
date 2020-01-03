from flask import Flask, render_template
app = Flask(__name__)


posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Eric TacoMaker',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}


]





@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title = 'Turtle', posts=posts) # set the render template



@app.route("/about")
def about():
	return render_template('about.html',title = 'About')

if __name__ == '__main__':  # run the Flask_App using python command 
	app.run(debug=True)
