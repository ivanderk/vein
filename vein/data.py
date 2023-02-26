

def get_user_by_name(user_name):
    "Searched for User from db by name. Must exist or generates exception"
    return db.session.execute(db.select(User).filter_by(name=user_name)).scalar_one()
   
def find_user_by_name(user_name):
    "Searched for User from db by name. Needs not to exist"
    return db.session.execute(db.select(User).filter_by(name=user_name)).scalar_one_or_none()
 