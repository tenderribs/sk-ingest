from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import uuid
import enum


class MeasurementType(enum.Enum):
    wind_speed_ms = 1
    east_wind_speed_ms = 2
    wind_speed_max_ms = 3
    humidity_pct = 4
    north_wind_speed_ms = 5
    irradiation_wm2 = 6
    wind_direction_deg = 7
    pressure_hpa = 8
    temperature_c = 9
    battery_voltage_v = 10


class Provider(enum.Enum):
    ugz_intern = 1
    innet = 2
    meteoblue = 3
    awel = 4


class Site(db.Model):
    __tablename__ = "sites"
    id = db.Column(db.Integer, primary_key=True)

    provider = db.Column(db.Enum(Provider), nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    wgs84_lat = db.Column(db.Float, nullable=False)
    wgs84_lon = db.Column(db.Float, nullable=False)
    masl = db.Column(db.Float, nullable=False)

    installations = db.relationship("Installation", backref="site", lazy=True)


class Installation(db.Model):
    __tablename__ = "installations"
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey("sites.id"), nullable=False)
    logger_id = db.Column(db.Integer, db.ForeignKey("loggers.id"), nullable=False)

    technician = db.Column(db.String, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=True)

    measurement = db.relationship("Measurement", backref="installation", lazy=True)


class Logger(db.Model):
    __tablename__ = "loggers"
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey("models.id"), nullable=False)

    sensor_id = db.Column(
        db.String(100), unique=True, nullable=False, default=lambda: str(uuid.uuid4())
    )
    sensor_serial = db.Column(
        db.String(100), unique=True, nullable=False, default=lambda: str(uuid.uuid4())
    )

    installation = db.relationship("Installation", backref="logger", lazy=True)
    measurement = db.relationship("Measurement", backref="logger", lazy=True)


class Model(db.Model):
    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False, unique=True)
    interval_s = db.Column(db.Integer, nullable=False, default=600)

    installation = db.relationship("Logger", backref="model", lazy=True)


class Measurement(db.Model):
    __tablename__ = "measurements"
    id = db.Column(db.Integer, primary_key=True)
    logger_id = db.Column(db.Integer, db.ForeignKey("loggers.id"), nullable=False)
    installation_id = db.Column(db.Integer, db.ForeignKey("installations.id"), nullable=False)

    measurement_type = db.Column(db.Enum(MeasurementType), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
