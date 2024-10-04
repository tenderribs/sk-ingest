import flask
from flask_migrate import Migrate

from env import db_url

from models import db

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CATCH_EXCEPTIONS"] = True

# https://github.com/miguelgrinberg/Flask-Migrate
migrate = Migrate(app, db)

# Create the database tables.
db.create_all()

# start the flask loop
app.run()
