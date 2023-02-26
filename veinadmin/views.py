
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template

from vein.models import Project, User

def init_admin(app, db):

    admin = Admin(app)

    class UserForm(FlaskForm):
        login = StringField('Login', validators=[DataRequired()])
        name = StringField('Name', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired()])
        password_hash = StringField('Password hash', validators=[DataRequired()])
        password_salt = StringField('Password salt', validators=[DataRequired()])
        submit = SubmitField('Submit')

    class ProjectForm(FlaskForm):
        name = StringField('Name', validators=[DataRequired()])
        submit = SubmitField('Submit')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Project, db.session))