from flask import Flask

from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db.init_app(app)

# perform migration if CLI cmd issued
migrate = Migrate(app, db)


if __name__ == "__main__":
    # start the flask loop
    app.run(host="0.0.0.0", port=8000)
