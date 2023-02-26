import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    return db
    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login= db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    password_salt = db.Column(db.String(128), nullable=False)
    projects = db.relationship('Project', secondary='user_project', back_populates='users')

    def set_password(self, password):
        # Generate a random salt
        salt = bcrypt.gensalt()

        # Hash the password using the salt and the bcrypt algorithm
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Store the salt and the hashed password in the database
        self.password_salt = salt.decode('utf-8')
        self.password_hash = password_hash.decode('utf-8')

    def check_password(self, password):
        # Hash the password using the stored salt and the bcrypt algorithm
        password_hash = bcrypt.hashpw(password.encode('utf-8'), self.password_salt.encode('utf-8'))

        # Compare the hashed password to the stored password hash
        return password_hash == self.password_hash.encode('utf-8')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surveys = db.relationship('Survey', backref='project')
    users = db.relationship('User', secondary='user_project', back_populates='projects')
    

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    respondents = db.relationship('Respondent', backref='survey')
 

class Respondent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)

user_project = db.Table('user_project',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)