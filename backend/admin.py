from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app, name="microblog", theme=Bootstrap4Theme(swatch="cerulean"))
# Add administrative views here

app.run()
