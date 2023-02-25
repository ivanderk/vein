from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from vein.views import vein_bp
#from veinadmin.views import veinadmin_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vein.db'
#app.config['EXPLAIN_TEMPLATE_LOADING'] = True
db = SQLAlchemy(app)


app.register_blueprint(vein_bp)
#app.register_blueprint(veinadmin_bp, url_prefix='/admin')

app.app_context().push()
db.create_all()

@app.route('/')
def index():
    #return redirect(url_for('vein.index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
