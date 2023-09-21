from flask import Flask
app = Flask(__name__) # __name__ is special variable that is the name of the module, here we are creating an instance of Flask

@app.route("/") # then use the route() decorator to tell Flask what URL should trigger our function. / is the root page/homepage of our website
@app.route("/home")
def home():
    return "<h2>Home page</h2>"

@app.route("/about")
def about():
    return "<h2>About Page</2>"
if __name__ == "__main__":
    app.run(debug=True) # Helps your site's changes to take effect, even without stopping and running the application again
    