from flask import Flask, render_template
from flask_migrate import Migrate
from app.models import db, Lanzamiento

app = Flask(__name__, template_folder='app/templates')

# CONFIG BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/datos_cohete"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar DB y migraciones
with app.app_context():
    db.init_app(app)
    migrate = Migrate(app, db)

@app.route('/inicio')
def inicio():
    lanzamientos = Lanzamiento.query.all()
    
    data = []
    
    for cohete in lanzamientos:
        data.append({
            'id': cohete.id,
            'lanzamiento': cohete.lanzamiento,
            'timestamp_ms': cohete.timestamp_ms,
            'pressure_pa': cohete.pressure_pa,
            'temp_c': cohete.temp_c,
            'altitude_asl_m': cohete.altitude_asl_m,
            'altitude_rel_m': cohete.altitude_rel_m,
            'vertical_speed_m_s': cohete.vertical_speed_m_s,
            'maxAltitude_rel': cohete.maxAltitude_rel
        })
    
    return render_template('inicio.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)