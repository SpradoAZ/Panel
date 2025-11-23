from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Lanzamiento(db.Model):
    __tablename__ = 'lanzamientos'

    id = db.Column(db.Integer, primary_key=True)
    lanzamiento = db.Column(db.Integer, nullable=False)
    timestamp_ms = db.Column(db.Float, nullable=True)
    pressure_pa = db.Column(db.Float, nullable=True)
    temp_c = db.Column(db.Float, nullable=True)
    altitude_asl_m = db.Column(db.Float, nullable=True)
    altitude_rel_m = db.Column(db.Float, nullable=True)
    vertical_speed_m_s = db.Column(db.Float, nullable=True)
    maxAltitude_rel = db.Column(db.Float, nullable=True)
