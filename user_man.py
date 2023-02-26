import getpass
from vein.models import User
from vein.data import find_user_by_name
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select

# Set up the database connection (NO ES IGUAL A FLASK. NO ESTAMOS EN UN PROCESO DE FLASK AHORA!!!!)
engine = create_engine('sqlite:///./instance/tasks.db')

# Create a new session factory
Session = sessionmaker(bind=engine)

def create_user(username, password):
    
    login = username.lower()
    # Create user with username (Lower case)
    user = User(name=login)
    # Hash the password (Lower) using the User model's set_password method
    user.set_password(password)

    # Add the user to the database
    session = Session()
    session.add(user)

    try:
        session.commit()
        print(f'User "{login}" created successfully')
    except IntegrityError:
        session.rollback()
        print(f'User "{login}" already exists')

def update_password(username, password):
    # Retrieve the user from the database
    login = username.lower()
    session = Session()
    user = session.execute(select(User).filter_by(name=login)).scalar_one_or_none()

    if user:
        
        # Hash the new password using the User model's set_password method
        user.set_password(password)

        # Update the user's password in the database
        session.commit()
        print(f'Password updated successfully for user "{login}"')
    else:
        print(f'User "{login}" not found')

if __name__ == '__main__':
    action = input('What would you like to do? (create/update) ')

    if action in 'create':
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')
        create_user(username, password)
    elif action in 'update':
        username = input('Enter username: ')
        password = getpass.getpass('Enter new password: ')
        update_password(username, password)
    else:
        print('Invalid action')
