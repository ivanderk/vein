from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from vein.data import find_user_by_user_name
from vein.middleware import authenticate_handler
from vein.views import vein_bp
from vein.models import init_app 
#from veinadmin.views import veinadmin_bp
from veinadmin.views import init_admin

app = Flask(__name__)

# The SECRET_KEY is used to encrypt session data in (persistent) cookies. 
# >>> import secrets; secrets.token_hex(32)
app.config['SECRET_KEY'] = '642918690903c342d812d16cd33a4de4c8692483462550c9ddcd4303621cc1b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vein.db'
#app.config['EXPLAIN_TEMPLATE_LOADING'] = True
db = init_app(app)
app.register_blueprint(vein_bp)
#app.register_blueprint(veinadmin_bp)
init_admin(app, db)

app.app_context().push()
db.create_all()

@app.before_request
def before_request():
    return authenticate_handler(None)

@app.after_request
def after_request(response):
    return authenticate_handler(response)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = find_user_by_user_name(username)
        
        if user is None or not user.check_password(password):
            error = 'Invalid username or password'
        else:
            #Note: Flask session. NOT SqlAlchemy...
            session['CURRENT_USER'] = (user.id, user.login)
            return redirect(url_for('vein.index'))

    return render_template('login.html', error=error)

@app.route('/logout', methods=['GET'])
def logout():
   
    #Note: Flask session. NOT SqlAlchemy...
    del session['CURRENT_USER'] 
    return redirect(url_for('login'))

@app.route('/')
def index():
    return redirect(url_for('vein.index'))

@app.route('/admin', methods=['GET'])
def admin():
   
    return redirect("/admin/")

@app.route('/page-not-found')
def page_not_found():
    return render_template('404.html')
  

if __name__ == '__main__':
    app.run(debug=True)
