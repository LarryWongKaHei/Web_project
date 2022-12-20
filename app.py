from flask import Flask, render_template, session

app = Flask(__name__)

# To import the blueprint from controllers file to register them
from controllers.Classes_controller import classes_blueprint
from controllers.Members_controller import members_blueprint
from controllers.Login_controller import Login_blueprint
from controllers.admin_controller import admin_blueprint

# To register blueprint
app.register_blueprint(classes_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(Login_blueprint)
app.register_blueprint(admin_blueprint)

# To set a key for session
app.secret_key = 'BAD_SECRET_KEY'

# Set up a Home Page
@app.route("/")
def index():
    return render_template("index.html")

# To make sure functions only run on main page
if __name__ == "__main__":
    app.run(debug=True)

