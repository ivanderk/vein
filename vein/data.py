
from .models import Project, Survey, Ticket, db, User


questions = [
    "My enthusiasm regarding the work I do...",
    "The Teamwork atmosphere and communication during the last sprints were...",
    "To what extent the tasks were challenging enough for me...",
    "I would rate my value contributed to the team as follows...",
    "The workload of this/the last sprint was...",
    "I feel supported by the client and stakeholders...",
    "I feel recognized and praised by the team...",
    "I feel inspired and excited to work in this team for the coming sprints..."
]

# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/
# https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html


def get_user_by_user_name(user_name):
    "Searched for User from db by name. Must exist or generates exception"
    return db.session.execute(db.select(User).filter_by(login=user_name)).scalar_one()


def find_user_by_user_name(user_name):
    "Searched for User from db by name. Needs not to exist"
    return db.session.execute(db.select(User).filter_by(login=user_name)).scalar_one_or_none()


def get_pending_surveys(user_name):

    user = get_user_by_user_name(user_name)

    return db.session.execute(db.select(Survey).join(Survey.tickets)
                              .where((Survey.closed == False) & (Ticket.completed == False) & (Ticket.user_id == user.id))).scalars()


def get_survey_from_id(id):
    return db.session.execute(db.select(Survey).filter_by(id=id)).scalar_one_or_none()
