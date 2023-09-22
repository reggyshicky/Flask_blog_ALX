from flask import Flask, render_template
app = Flask(__name__) # __name__ is special variable that is the name of the module, here we are creating an instance of Flask

posts = [
    {
        'author': 'Reggy',
        'title':  'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Shicky',
        'title':  'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2023'
    }
]
@app.route("/") # then use the route() decorator to tell Flask what URL should trigger our function. / is the root page/homepage of our website
@app.route("/home") #this two routes are being handled by the same function
def home():
    return render_template("home.html", posts=posts) # first post is a variable, which is gonna be equal to the posts data above

@app.route("/about")
def about():
    return render_template("about.html", title='About')
if __name__ == "__main__":
    app.run(debug=True) # Helps your site's changes to take effect, even without stopping and running the application again
    