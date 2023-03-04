from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template

from vein.models import Project, Survey, User


class UserAdminView(ModelView):
    column_searchable_list = ['login', 'name']
    form_columns = ['login', 'name', 'email']


class ProjectAdminView(ModelView):
    column_searchable_list = ['name']
    form_columns = ['name']


class SurveyAdminView(ModelView):
    column_searchable_list = ['title']
    form_columns = ['title', 'status', 'rating', 'mood', 'completed']

def init_admin(app, db):

    admin = Admin(app, name='Vein admin')  # , template_mode='bootstrap3')
    admin.add_view(UserAdminView(User, db.session))
    admin.add_view(ProjectAdminView(Project, db.session))
    admin.add_view(SurveyAdminView(Survey, db.session))
