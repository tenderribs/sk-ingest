from flask import Flask

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Site, Installation, Logger, Model, Measurement

app = Flask(__name__)


# Add Flask-Admin
admin = Admin(app=app, name="SuperAdmin", template_mode="bootstrap3")

# Add models to Flask-Admin
admin.add_view(ModelView(Site, db.session))
admin.add_view(ModelView(Installation, db.session))
admin.add_view(ModelView(Logger, db.session))
admin.add_view(ModelView(Model, db.session))
admin.add_view(ModelView(Measurement, db.session))

if __name__ == "__main__":
    admin.app.run(host="0.0.0.0", port=4000)
