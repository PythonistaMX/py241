from apiflask import APIFlask
from models import db, Alumno, User
from blueprints import abc_alumnos
from auth.blueprints import auth_bp

app = APIFlask(__name__)
app.config.from_pyfile("settings.py")
db.init_app(app)  

@app.before_first_request
def crea_bases():
    db.create_all()
    # Crea y llena la base de alumno.
    with open("data/alumnos.txt", "rt") as f:
        alumnos = eval(f.read())
        for alumno in alumnos:
            db.session.add(Alumno(**alumno))
        db.session.commit()

    user = User(username='admin', email='example@example.com',password='admin', active=True)
    db.session.add(user)
    db.session.commit() 

app.register_blueprint(abc_alumnos, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)