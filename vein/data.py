
from .models import Answer, Project, Survey, Ticket, db, User


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


def get_user_by_id(id):
    "Searched for User from db by id. Must exist or generates exception"
    return db.session.execute(db.select(User).filter_by(id=id)).scalar_one()

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


def get_ticket_by_id(id):
    return db.session.execute(db.select(Ticket).filter_by(id=id)).scalar_one()

def get_survey_by_id(id):
    return db.session.execute(db.select(Survey).filter_by(id=id)).scalar_one()

def save_survey_answer_by_id(survey_id, user_id, answer):
    
    survey = get_survey_by_id(survey_id)
    ticket = next(ticket for ticket in survey.tickets if ticket.id==user_id)
    ticket.completed = True
    
    answer = Answer(data=answer, survey_id=survey_id)
    db.session.add(answer)
    db.session.commit()
    

def extract_answer(form):
    answer_lst = ['0' for e in range(0,9)]
    answer_lst[8] = form.get('rating-base')
    for i in range(0,8):
        answer_lst[i] = form.get(f'rating-{i}')
    
    print(answer_lst)
    return '-'.join(answer_lst) 
    